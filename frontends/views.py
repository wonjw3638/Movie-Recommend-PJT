from django.shortcuts import render

def index(request):
    return render(request, 'frontends/index.html')

def choice(request):
    return render(request, 'frontends/choice.html')

def trailer(request):
    return render(request, 'frontends/trailer.html')

def result(request):
    return render(request, 'frontends/result.html')