from django.db import models


class News(models.Model):
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
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

