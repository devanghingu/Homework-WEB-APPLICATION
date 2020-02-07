from django import forms
from django.contrib.auth.forms import AuthenticationForm, authenticate, UserCreationForm
from .models import User,CleanerProfile,City
from django.core.validators import validate_email
class signupform(UserCreationForm):
    # password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields=('contact', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(signupform,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control','placeholder': self.fields[field].label})
    def clean_contact(self):
        contact=self.cleaned_data['contact']
        if len(contact)<9 and contact.isnumeric():
            raise forms.ValidationError("contact number must have 10 digit number")
        return contact

class Loginform(AuthenticationForm):
    class Meta:
        model=User
        fields=['contact','password']
    def __init__(self, *args, **kwargs):
        super(Loginform,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder': self.fields[field].label})
    
    def clean_contact(self):
        contact=self.cleaned_data['contact']
        print('validation working')
        if len(contact)>9 and contact.__class__ == 'int':
            raise forms.ValidationError("contact number must have 10 digit number")
        return contact
    
class CleanerForm(forms.Form):
    city=forms.ModelChoiceField(queryset=City.objects.all(),label='select preferred city')
    address=forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}),label="Address")

    pincode=forms.IntegerField(required=False,label='Pincode')
    class Meta:
        model=CleanerProfile
        fields=['city','address','pincode']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder': self.fields[field].label})

    def clean_city(self):
        city=self.cleaned_data['city']
        data=City.objects.get(name=city)
        if data:
            return city
        raise forms.ValidationError("select city in available city")
    def clean_pincode(self):
        pincode = self.cleaned_data["pincode"]
        print(type(pincode))
        if not pincode.__class__!='int':
            raise forms.ValidationError("pincode must be in numbers")
        if len(str(pincode)) != 6:
            raise forms.ValidationError("pincode must 6 digit")
        return pincode
    