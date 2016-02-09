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
            return redirect('listing', profile.pk)
    else:
        form = JobListingForm()

    context = {
        "form": form
    }

    return render(request, "createjoblisting.html", context)

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
        form = JobListingForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('listing', post.pk)

    else:
        form = JobListingForm(instance=post)

    context = {
        "form": form,
        "post": post
    }

    return render(request, "editlisting.html", context)

@login_required(redirect_field_name='login')
def editlistingportal(request):

    account_owner = request.user
    job_listings = JobListing.objects.filter(user=account_owner).exclude(active_listing=False)

    context = {'joblistings': job_listings}

    return render(request, "editlistingportal.html", context)

@login_required(redirect_field_name='login')
def deletelistingconfirm(request, pk):

    post = JobListing.objects.get(pk=pk)

    if str(request.user) != str(post.user):
        return redirect("index")

    context_dict = {'post': post}

    return render(request, 'delete_listing_confirm.html', context_dict)

@login_required(redirect_field_name='login')
def deletefunction(request, pk):

    post = JobListing.objects.get(pk=pk)

    if str(request.user) != str(post.user):
        return redirect("permissiondenied")

    post.active_listing = True
    post.save()

    return redirect('editlistingportal')

    context_dict = {}

    return render(request, 'delete_function.html', context_dict)