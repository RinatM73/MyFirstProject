from django.shortcuts import render

def videoview(request):
    return render(request, 'video/video.html')
