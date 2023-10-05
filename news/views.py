from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import News # подключение базы данных
app_name = 'news'
# Create your views here.
def news(request):
    news = News.objects.all() # отвечает за хранение подключенной базы
    return render(request, template_name='news/news.html', context={'news':news})

def news_det(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news_det/news_det.html', {'news':news})

def news_comment(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        formc = CommentForm(request.POST)
        if formc.is_valid():
            comment = formc.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news', pk=news.pk)
    else:
        formc = CommentForm()
    return render(request, 'news_comment/news_comment.html', {'formc': formc})
