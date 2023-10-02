# Generated by Django 5.0a1 on 2023-10-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='photo/image/', verbose_name='Фото')),
                ('desc_1', models.TextField(verbose_name='Описание')),
                ('date_2', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]
