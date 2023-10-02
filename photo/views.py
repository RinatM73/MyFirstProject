from django.shortcuts import render
from .models import Photo

def photoview(request):
    photo = Photo.objects.all()
    return render(request, 'photo/photo.html', {'photo':photo})
