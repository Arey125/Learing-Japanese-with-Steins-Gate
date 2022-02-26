from django.db import models
# Create your models here.


class File(models.Model):
    filename = models.CharField(max_length=50, unique=True)


class Sentence(models.Model):
    index = models.IntegerField(default=0)
    sentence = models.CharField(max_length=200)
    file = models.ForeignKey(File, on_delete=models.PROTECT)
    merged = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    exported = models.BooleanField(default=False)


class Translation(models.Model):
    index = models.IntegerField(default=0)
    translation = models.CharField(max_length=400)
    audio = models.CharField(max_length=200)
    file = models.ForeignKey(File, on_delete=models.PROTECT)


class Word(models.Model):
    word = models.CharField(max_length=50, unique=True)
    translation = models.CharField(max_length=50)
    pronounce = models.CharField(max_length=50)
    sentence = models.ForeignKey(Sentence, on_delete=models.PROTECT)
