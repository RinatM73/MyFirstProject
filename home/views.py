from django.shortcuts import render

from news.models import News
from video.models import Video


def home(request):
    news = News.objects.all()
    videos = Video.objects.all()
    return render(request, 'home/home.html', {'news_list': news, 'video_list': videos})


