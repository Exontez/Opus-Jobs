from django.shortcuts import render

def index(request):

    context_dict = {}

    return render(request, 'index.html', context_dict)

def about(request):

    context_dict = {}

    return render(request, 'about.html', context_dict)
