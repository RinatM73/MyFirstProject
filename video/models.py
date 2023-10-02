from django.db import models

class Video(models.Model):
    video = models.FileField('Видео', upload_to='video/video/')
    desc_2 = models.TextField('Описание')
    date_3 = models.DateField('Дата')

    def __str__(self):
        return f"{self.desc_2} | {self.date_3}"

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'
