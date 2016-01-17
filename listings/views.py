from django.shortcuts import render
from profiles.models import JobListing

# This is the view function for displaying the browse page
def browse(request):

    job_listings = JobListing.objects.exclude(active_listing=False)

    context_dict = {'joblistings': job_listings}

    return render(request, 'browse.html', context_dict)

def listing(request, pk):

    job_listing = JobListing.objects.get(pk=pk)

    context_dict = {'joblistings': job_listing}

    return render(request, 'listing.html', context_dict)