# Generated by Django 3.2.16 on 2022-11-23 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Video',
        ),
    ]