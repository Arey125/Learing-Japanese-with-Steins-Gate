# Generated by Django 3.2.6 on 2021-08-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_translation_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='merged',
            field=models.BooleanField(default=False),
        ),
    ]
