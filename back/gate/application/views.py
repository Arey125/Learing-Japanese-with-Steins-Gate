from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max


def index(request):
    files_query = File.objects.all()
    is_checked = [{"checked": file.sentence_set.filter(checked=True).exists()}
                  for file in files_query]
    files = File.objects.all().values()
    files = [{**file, **checked}
             for file, checked in zip(files, is_checked)]
    data = {'data': files}
    return JsonResponse(data)


def merge_items(sent, next_sent):
    if not sent['sentence'][-1] in '。？！':
        sent['sentence'] += '。'
    sent['sentence'] += next_sent['sentence']
    sent['merged'] = next_sent['merged']


def __get_file(file_id):
    if file_id != 'all':
        file = File.objects.get(id=file_id)
        file.sentence_set
        sent_val = list(Sentence.objects.filter(file=file).values())
        transl = list(Translation.objects.filter(file=file).values())
    else:
        sent_val = list(Sentence.objects.all().values())
        transl = list(Translation.objects.all().values())

    sent_sorted = sorted(sent_val, key=lambda x: x['id'])
    sent = []
    diff = 0
    for item in sent_sorted:
        if sent == [] or not sent[-1]['merged']:
            item['index'] -= diff
            sent.append(item)
            continue
        merge_items(sent[-1], item)
        diff += 1

    transl = sorted(transl, key=lambda x: x['id'])

    resp = [
        dict(list(t.items()) + list(s.items()))
        for s, t in zip(sent, transl)
        if file_id != 'all' or (s['checked'] and not s['exported'])
    ]
    return list(resp)


def get_file(request):
    file_id = request.GET.get('id')
    return JsonResponse({'data': __get_file(file_id)})


def get_sentence(request):
    sent_id = request.GET.get('id')
    sent = Sentence.objects.get(id=sent_id)
    resp = Word.objects.filter(sentence=sent).values()

    data = {'words': list(resp), 'sentence': sent.values()}
    return JsonResponse(data)


def merge(request):
    sent_id = request.GET.get('id')
    sent = Sentence.objects.get(id=sent_id)
    sent.merged = True
    sent.save()
    return HttpResponse('')


def split(request):
    sent_id = request.GET.get('id')
    sent = Sentence.objects.get(id=sent_id)
    sent.merged = False
    sent.save()
    return HttpResponse('')


def get_voice(request, name):
    file = open(f'voice/{name}.ogg', 'rb')
    return FileResponse(file)


def mark(request):
    sent_id = request.GET.get('id')
    sent = Sentence.objects.get(id=sent_id)
    sent.checked = not sent.checked
    sent.save()
    return JsonResponse({'data': __get_file(sent.file_id)})


def export(request):
    data = __get_file('all')
    with open('export.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join([
            '\t'.join([
                f"[sound:{sent['audio'].split('/')[1]}.ogg]",
                sent['sentence'],
                sent['translation']
            ])
            for sent in data
        ]))
    file = open('export.txt', 'rb')
    return FileResponse(file, filename='export.txt')


@csrf_exempt
def upload_db(request):

    json_data = json.loads(request.POST['upload'])
    print(json_data.keys())
    files = json_data['files']
    sentences = json_data['sentences']
    translations = json_data['translations']

    for file in files:
        name = file['name']
        if File.objects.filter(filename=name).exists():
            continue
        f = File(filename=name)
        f.save()

    for sentence in sentences:
        ind = sentence['index']
        sentence_str = sentence['sentence']
        file = sentence['file']
        sent = Sentence(
            index=ind,
            sentence=sentence_str,
            file=File.objects.get(filename=file),
        )
        sent.save()

    for translation in translations:
        ind = translation['index']
        translation_str = translation['translation']
        audio = translation['audio']
        file = translation['file']
        transl = Translation(
            index=ind,
            translation=translation_str,
            audio=audio,
            file=File.objects.get(filename=file),
        )
        transl.save()

    return HttpResponse('')
