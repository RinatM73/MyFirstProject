from django.shortcuts import render, get_object_or_404

from .models import Article # подключение базы данных
app_name = 'news'
# Create your views here.
def newsView(request):
    articles = Article.objects.all() # отвечает за хранение подключенной базы
    print(articles[0].desc)
    return render(request, template_name='news/news.html', context={'articles':articles})