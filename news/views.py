from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import CommentForm
from .models import News, Comment  # подключение базы данных
app_name = 'news'
# Create your views here.
def news(request):
    news = News.objects.all() # отвечает за хранение подключенной базы
    return render(request, template_name='news/news.html', context={'news':news})

def news_det(request, pk):
    news = get_object_or_404(News, id=pk)
    comment = Comment.objects.filter(news=pk, moderation=True)
    if request.method == 'POST':
        formc = CommentForm(request.POST)
        if formc.is_valid():
            form = formc.save(commit=False)
            form.user = request.user
            form.news = news
            form.save()
            return redirect(news_det, pk)
    else:
        form = CommentForm()
    return render(request, 'news_det/news_det.html', {'news':news, 'comments':comment, 'form':form})

