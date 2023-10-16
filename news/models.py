from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField('Заголовок',max_length=100)     # Строка с огр знаками
    desc = models.TextField('Описание')      # Строка с огр знаками
    image = models.ImageField('Изображение',upload_to='news/image/')       # Строка под Изображение
    date = models.DateField('Дата')        # Дата
    url = models.URLField('Доп.источник', blank=True)        # Ссылка




    def __str__(self):
        return f"{self.title} | {self.date}"

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    text = models.TextField('Комментарий', blank=True)
    created_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    moderation = models.BooleanField('Модерация', default=False)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return  '{}'.format(self.user)

