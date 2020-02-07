from django import forms
from useractivity.models import User,CleanerProfile,City
from .models import bookings
from useractivity.models import City
import datetime
class NewBookingForm(forms.Form):
    CHOICES=(
        ('1','10 AM - 12 PM'),
        ('2','12 PM - 02 PM'),
        ('3','02 PM - 04 PM'),
        ('4','04 PM - 06 PM'),
        ('5','06 PM - 08 PM'))
    city=forms.ModelChoiceField(queryset=City.objects.all(),label='select preferred city')
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    slot=forms.ChoiceField(choices=CHOICES, required=True)
    date.widget.attrs['min']=datetime.date.today()
    class Meta:
        model= bookings
        fields=['city','date','slot']
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder': self.fields[field].label}) 
    def clean_city(self):
        city=self.cleaned_data['city']
        data=City.objects.get(name=city)
        if data:
            return city
        raise forms.ValidationError("select city in available cities.")
    
    def clean_slot(self):
        slot = self.cleaned_data["slot"]
        if int(slot) not in [1,2,3,4,5]:
            raise forms.ValidationError("select form available slots.")
        return slot
    def clean_date(self):
        date = self.cleaned_data["date"]
        if (date>=datetime.date.today()):
            return date
        raise forms.ValidationError("you cannot select past date.")
    