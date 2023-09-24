from django.shortcuts import render

def resultsview(request):
    return render(request, 'results/results.html')
