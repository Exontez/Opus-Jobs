from django.shortcuts import render
from forms import JobListingForm, SignupForm
from django.contrib.auth.models import User
from models import SignUpProfile, JobListing
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# This is the view which manages the create job listing page
@login_required(redirect_field_name='login')
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

#ADD A REDIRECT AFTER THIS PAGE

# This is the view which manages the edit profile page
@login_required(redirect_field_name='login')
def editprofile(request, pk):

    post = SignUpProfile.objects.get(pk=pk)
    post2 = User.objects.all()

    if request.method == "POST":
        form = SignupForm(request.POST, instance=post)

    else:
        form = SignupForm(instance=post)

    context = {
        "form": form
    }

    return render(request, "editprofile.html", context)

# This is the view which manages the edit listing page
@login_required(redirect_field_name='login')
def editlisting(request, pk):

    post = JobListing.objects.get(pk=pk)

    if str(request.user) != str(post.user):
        return redirect("index")

    if request.method == "POST":
        print("test")
        form = JobListingForm(request.POST, instance=post, force_update=True)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        print("else")
        form = JobListingForm(instance=post)

    context = {
        "form": form
    }

    return render(request, "editlisting.html", context)

@login_required(redirect_field_name='login')
def editlistingportal(request):

    account_owner = request.user
    job_listings = JobListing.objects.filter(user=account_owner).exclude(active_listing=False)
    test = JobListing.objects.exclude(active_listing=False)
    print(test)

    context = {'joblistings': job_listings}

    return render(request, "editlistingportal.html", context)