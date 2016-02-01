from django.shortcuts import render
from listings.forms import JobQuickSearchForm

def index(request):

    form = JobQuickSearchForm()

    context_dict = {
        "form": form
    }

    return render(request, 'index.html', context_dict)

def about(request):

    context_dict = {}

    return render(request, 'about.html', context_dict)

def credits(request):

    context_dict = {}

    return render(request, 'credits.html', context_dict)

def featurenotimplemented(request):

    context_dict = {}

    return render(request, 'feature_notimplemented.html', context_dict)
