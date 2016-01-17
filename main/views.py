from django.shortcuts import render

# This is my index page view
def index(request):

    context_dict = {}

    return render(request, 'index.html', context_dict)

# This is my about page view
def about(request):

    context_dict = {}

    return render(request, 'about.html', context_dict)

# This is my feature not implemented page
def featurenotimplemented(request):

    context_dict = {}

    return render(request, 'feature_notimplemented.html', context_dict)
