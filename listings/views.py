from django.shortcuts import render
from profiles.models import JobListing
from forms import JobSearchForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# This is the view function for displaying the browse page
def browse(request):

    business_industry = request.GET.get('business_industry', '')
    business_address_region = request.GET.get('business_address_region', '')
    employment_type = request.GET.get('employment_type', '')
    pay_rate = request.GET.get('pay_rate', '')
    keywords = request.GET.get('keywords', '').split()

    form = JobSearchForm(initial=request.GET)

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
        filters &= reduce(lambda x, y: x & y, [Q(job_description__icontains=word) for word in keywords]) | reduce(lambda x, y: x & y, [Q(job_title__icontains=word) for word in keywords])

    job_listings_list = JobListing.objects.filter(filters).distinct().order_by('-listing_date')

    paginator = Paginator(job_listings_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')

    try:
        job_listings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        job_listings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        job_listings = paginator.page(paginator.num_pages)

    current_page_start = job_listings.start_index()
    current_page_end = job_listings.end_index()

    before_current_pages = 4
    after_current_pages = 4
    before = max(job_listings.number - before_current_pages - 1, 0)
    after = job_listings.number + after_current_pages
    page_range = list(job_listings.paginator.page_range)
    middle = page_range[before:after]

    queries_without_page = request.GET.copy()
    if 'page' in queries_without_page:
        del queries_without_page['page']

    context_dict = {
        'joblistings': job_listings,
        'job_listings_list': job_listings_list,
        'current_page_start': current_page_start,
        'current_page_end': current_page_end,
        'form': form,
        'middle': middle,
        'queries': queries_without_page,
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