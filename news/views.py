from django.shortcuts import render, get_object_or_404

from .models import News # подключение базы данных
app_name = 'news'
# Create your views here.
def news(request):
    news = News.objects.all() # отвечает за хранение подключенной базы
    return render(request, template_name='news/news.html', context={'news':news})