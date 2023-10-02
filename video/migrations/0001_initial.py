# Generated by Django 5.0a1 on 2023-10-02 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/video/', verbose_name='Видео')),
                ('desc_2', models.TextField(verbose_name='Описание')),
                ('date_3', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
