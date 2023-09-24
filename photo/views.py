from django.shortcuts import render

def photoview(request):
    return render(request, 'photo/photo.html')
