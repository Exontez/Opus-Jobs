from django.shortcuts import render
from forms import JobListingForm

def createjoblisting(request):

    form = JobListingForm()
    context = {
        "form": form
    }

    return render(request, "createjoblisting.html", context)
