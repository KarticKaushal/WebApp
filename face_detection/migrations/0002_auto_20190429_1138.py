# Generated by Django 2.2 on 2019-04-29 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloak', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageuploadmodel',
            old_name='document',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='imageuploadmodel',
            name='description',
        ),
    ]
