from django.shortcuts import render
from video.models import Video

def videoview(request):
    video = Video.objects.all()
    return render(request, 'video/video.html', {'video':video})
