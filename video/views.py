from django.shortcuts import render, get_object_or_404
from video.models import Video

def videoview(request):
    video = Video.objects.all()
    return render(request, 'video/video.html', {'video':video})

def video_det(request, pk):
    video = get_object_or_404(Video, id=pk)
    return render(request, 'video_det/video_det.html', {'video_det': video})
