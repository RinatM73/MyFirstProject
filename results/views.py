from django.shortcuts import render

from results.models import Results


def results(request):
    results = Results.objects.all()
    return render(request, 'results/results.html', {'results': results})
