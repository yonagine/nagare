# Generated by Django 4.0.4 on 2022-05-04 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logentry', '0005_rename_logtime_listeninglogentry_log_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listeninglogentry',
            old_name='media',
            new_name='media_pk',
        ),
        migrations.RenameField(
            model_name='readinglogentry',
            old_name='media',
            new_name='media_pk',
        ),
    ]
