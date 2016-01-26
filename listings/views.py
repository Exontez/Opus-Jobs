from django.shortcuts import render
from profiles.models import JobListing
from forms import JobSearchForm

# This is the view function for displaying the browse page
def browse(request):

    business_industry = request.GET.get('business_industry', '')
    business_address_region = request.GET.get('business_address_region', '')
    keywords = request.GET.get('keywords', '')
    print(business_industry)
    print(business_address_region)
    print(keywords)

    if keywords is '':
        print("I HATE LIFT")

    if business_industry is '' and business_address_region is '' and keywords is '':
        print("If")
    else:
        print("Else")

    form = JobSearchForm()

    job_listings = JobListing.objects.exclude(active_listing=False)

    context_dict = {
        'joblistings': job_listings,
        'form': form
    }

    return render(request, 'browse.html', context_dict)

def listing(request, pk,):

    job_listing = JobListing.objects.get(pk=pk)

    def view_counter():
        view_count = job_listing.listing_view_counter
        job_listing.listing_view_counter = view_count + 1
        job_listing.save()
        print(view_count)

    view_counter()

    context_dict = {'joblistings': job_listing}

    return render(request, 'listing.html', context_dict)