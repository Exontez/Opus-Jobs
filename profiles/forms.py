from django import forms
from models import SignUpProfile, JobListing, User

# This is the form my extended signup model
class SignupForm(forms.Form):

    account_type = forms.ChoiceField(choices=SignUpProfile.account_type_choice)
    username = forms.CharField(max_length=10)
    email = forms.CharField(max_length=50, label='Test', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'First Name'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput, label='')
    first_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    contact_number = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))

    def signup(self, request, user):
        SignUpProfile.objects.get_or_create(
            user=user,
            account_type=self.cleaned_data['account_type'],
            contact_number=self.cleaned_data['contact_number']
        )

    class Meta:
        model = SignUpProfile

# This is code I am experimenting with
"""
class SignupForm(forms.ModelForm):

    username = forms.CharField(max_length=10)
    email = forms.CharField(max_length=50, label='Test', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'First Name'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput, label='')
    first_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = SignUpProfile, User
        fields = ['account_type', 'username', 'email', 'password1', 'password2', 'first_name',
            'last_name', 'contact_number']
"""

# This is my form for creating and edit job listings
class JobListingForm(forms.ModelForm):

    class Meta:
        model = JobListing
        fields = ['job_title', 'pay_rate', 'employment_type', 'job_description', 'business_address_region',
            'business_address_suburb', 'business_industry', 'telephone', 'email']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Job Title'}),
            'pay_rate': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Hourly Rate or One Off Amount'}),
            'employment_type': forms.Select(attrs={'class': 'form-input'}),
            'job_description': forms.Textarea(attrs={'class': 'form-textarea',
                'placeholder': 'Tell us additional information about your job listing e.g. Times, Business Info, Number of positions etc. (2000 Character Limit)'}),
            'business_address_region': forms.Select(attrs={'class': 'form-input'}),
            'business_address_suburb': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Business Suburb'}),
            'business_industry': forms.Select(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Contact Numnber'}),
        }







