# Generated by Django 4.0.4 on 2022-05-01 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('description', models.TextField(max_length=240, verbose_name='Description')),
                ('created', models.DateField(auto_now_add=True)),
                ('kind', models.CharField(choices=[('Reading', (('VN', 'Visual Novel'), ('LN', 'Light Novel'))), ('Listening', (('AN', 'Anime'), ('AU', 'Audio'))), ('NA', 'Unknown')], default='NA', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ListeningMedia',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='media.media')),
            ],
            bases=('media.media',),
        ),
        migrations.CreateModel(
            name='ReadingMedia',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='media.media')),
            ],
            bases=('media.media',),
        ),
    ]