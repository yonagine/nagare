# Generated by Django 4.0.4 on 2022-05-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readingmedia',
            name='media_ptr',
        ),
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.TextField(max_length=240, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(max_length=240, verbose_name='name'),
        ),
        migrations.DeleteModel(
            name='ListeningMedia',
        ),
        migrations.DeleteModel(
            name='ReadingMedia',
        ),
    ]
