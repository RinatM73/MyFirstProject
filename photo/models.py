from django.db import models

class Photo(models.Model):
    image_1 = models.ImageField('Фото', upload_to='photo/image/')
    desc_1 = models.TextField('Описание')
    date_2 = models.DateField('Дата')

    def __str__(self):
        return f"{self.desc_1} | {self.date_2}"

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'