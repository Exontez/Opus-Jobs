from django.shortcuts import render
from forms import JobListingForm
from django.http import HttpResponseRedirect

def createjoblisting(request):

    if request.method == "POST":

        form = JobListingForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect('index')
    else:
        form = JobListingForm()

    context = {
        "form": form
    }

    return render(request, "createjoblisting.html", context)
