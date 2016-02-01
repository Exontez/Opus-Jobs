from django import forms

region_choice = (
    ('', 'Region'),
    ('1', 'Auckland'),
    ('2', 'Wellington'),
    ('3', 'Christchurch')
)
suburb_choice = (
    ('', 'None'),
    ('1', 'Glendowie'),
    ('2', 'Kohimarama'),
    ('3', 'Herne Bay')
)
industry_choice = (
    ('', 'Business Industry'),
    ('1', 'Accounting'),
    ('2', 'Agriculture, fishing & forestry'),
    ('3', 'Automotive'),
    ('4', 'Banking, finance & insurance'),
    ('5', 'Construction & Architecture'),
    ('6', 'Customer service'),
)
employment_type_choice = (
    ('', 'None'),
    ('1', 'Full Time'),
    ('2', 'Part Time'),
    ('3', 'One-off'),
    ('4', 'Other')
)
pay_rate_choice = (
    ('1', 'None'),
    ('1', 'Full Time'),
    ('2', 'Part Time'),
    ('3', 'One-off'),
    ('4', 'Other')
)

class JobQuickSearchForm(forms.Form):
    business_address_region = forms.ChoiceField(region_choice, widget=forms.Select(attrs={'class': 'qs-form-input'}))
    business_industry = forms.ChoiceField(industry_choice, widget=forms.Select(attrs={'class': 'qs-form-input'}))
    keywords = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'qs-form-input', 'placeholder': 'Enter Keywords...'}))

class JobSearchForm(forms.Form):
    pay_rate_minimum = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'qsm-form-input', 'placeholder': 'Pay Rate'}))
    pay_rate_maximum = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'qsm-form-input', 'placeholder': 'Pay Rate'}))
    employment_type = forms.ChoiceField(employment_type_choice, widget=forms.Select(attrs={'class': 'qsm-form-input'}))
    business_address_region = forms.ChoiceField(region_choice, widget=forms.Select(attrs={'class': 'qsm-form-input'}))
    business_address_suburb = forms.ChoiceField(suburb_choice, widget=forms.Select(attrs={'class': 'qsm-form-input'}))
    business_industry = forms.ChoiceField(industry_choice, widget=forms.Select(attrs={'class': 'qsm-form-input', 'value': '{{ request.GET.business_industry }}'}))
    keywords = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'qsm-form-input', 'placeholder': 'Enter Keywords...'}))
