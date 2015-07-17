from django import forms
from models import SignUpProfile, JobListing

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
        SignUpProfile.objects.create(
            user=user,
            account_type=self.cleaned_data['account_type'],
            contact_number=self.cleaned_data['contact_number']
        )

    class Meta:
        model = SignUpProfile

class JobListingForm(forms.ModelForm):

    class Meta:
        model = JobListing
        fields = ['business_name', 'pay_rate', 'employment_type', 'job_description', 'business_address_region',
            'business_address_suburb', 'business_industry']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-input', 'required': 'true', 'placeholder': 'Name of Business'}),
            'pay_rate': forms.NumberInput(attrs={'class': 'form-input', 'required': 'true', 'placeholder': 'Hourly Rate or One Off Amount'}),
            'employment_type': forms.Select(attrs={'class': 'form-input', 'required': 'true'}),
            'job_description': forms.Textarea(attrs={'class': 'form-textarea', 'required': 'true',
                'placeholder': 'Tell us additional information about your job listing e.g. Times, Business Info, Number of positions etc. (2000 Character Limit)'}),
            'business_address_region': forms.Select(attrs={'class': 'form-input', 'required': 'true'}),
            'business_address_suburb': forms.TextInput(attrs={'class': 'form-input', 'required': 'true', 'placeholder': 'Business Suburb'}),
            'business_industry': forms.Select(attrs={'class': 'form-input', 'required': 'true'}),
        }







