from django import forms
from models import SignUpProfile

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

'''
class SignupForm(forms.Form):

    business_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Business Name'}))
    business_address_number = forms.IntegerField(label='',
                                                 widget=forms.TextInput(attrs={'placeholder': 'Street Number'}))
    business_address_street = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Street Name'}))
    business_address_region = forms.ChoiceField(choices=EmployerProfile.region_choice, label='')
    business_address_suburb = forms.ChoiceField(max_length='50')
    business_address_postcode = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Postcode'}))
    business_industry = forms.ChoiceField(choices=EmployerProfile.industry_choice, label='')

    def signup(self, request, user):
        EmployerProfile.objects.create(
            user=user,
            home_number=self.cleaned_data['home_number'],
            mobile_number=self.cleaned_data['mobile_number'],
            business_name=self.cleaned_data['business_name'],
            business_address_number=self.cleaned_data['business_address_number'],
            business_address_street=self.cleaned_data['business_address_street'],
            business_address_region=self.cleaned_data['business_address_region'],
            business_address_suburb=self.cleaned_data['business_address_suburb'],
            business_address_postcode=self.cleaned_data['business_address_postcode'],
            business_industry=self.cleaned_data['business_industry']
        )

    class Meta:
        model = EmployerProfile
'''






