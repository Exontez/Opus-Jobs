from django.shortcuts import render
from profiles.models import JobListing
from forms import JobSearchForm
from django.db.models import Q

# This is the view function for displaying the browse page
def browse(request):

    business_industry = request.GET.get('business_industry', '')
    business_address_region = request.GET.get('business_address_region', '')
    employment_type = request.GET.get('employment_type', '')
    pay_rate = request.GET.get('pay_rate', '')
    keywords = request.GET.get('keywords', '')
    print('business_industry =', business_industry)
    print('business_region =', business_address_region)
    print('keywords =', keywords)
    print('pay rate =', pay_rate)
    print('employment_type =', employment_type)

    form = JobSearchForm()

    filters = Q(active_listing=True)

    if business_industry:
        filters &= Q(business_industry=business_industry)
    if business_address_region:
        filters &= Q(business_address_region=business_address_region)
    if employment_type:
        filters &= Q(employment_type=employment_type)
    if pay_rate:
        filters &= Q(pay_rate=pay_rate)
    if keywords:
        filters &= Q(job_description__icontains=keywords, job_title__icontains=keywords)
    print(filters)

    job_listings = JobListing.objects.filter(filters).distinct()

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