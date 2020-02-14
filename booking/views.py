from django.shortcuts import render,redirect
from django.views import View
from .models import bookings
from useractivity.models import User,CleanerProfile,City
from .forms import NewBookingForm
from django.contrib import messages
# Create your views here.
# mybooking
# newbooking
# global CHOICE= [1,2,3,4,5]
class bookingchecker():
    @classmethod
    def check(self):
        pass
class Newbooking(View):
    def get(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,'pelase login to book your cleaner expert')
            return redirect('login')
        form=NewBookingForm()
        print(args,kwargs)
        context={'form':form,'title':'Find Best Clean Expert'}
        return render(request,'booking.html',context)
    def post(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,'pelase login to book your cleaner expert')
            return redirect('login')
        form=NewBookingForm(request.POST)
        context={'form':form,'title':'Find Best Clean Expert'}
        
        if form.is_valid():
            city=form.cleaned_data['city']
            date=form.cleaned_data['date']
            slot=form.cleaned_data['slot']
            # print(slot,'-----')
            # cleaner=CleanerProfile.objects.filter(working_city=city)
            bookingdata=bookings.objects.filter(city=city,timeslot=slot,dateofcleaning=date)  #all cleaner who working in selected city
            # print([x.customer_id for x in bookingdata])
            cleaner=CleanerProfile.objects.filter(working_city=city).exclude(user__in=[x.cleaner_id.user for x in bookingdata]).exclude(user=request.user).exclude(user__email='')
            if (cleaner.exists()==True):
                request.session['city']=str(city)
                request.session['date']=str(date)
                request.session['slot']=str(slot)
                context['allcleaner']=cleaner
            else:
                messages.error(request,"opps clean expert doen't exist..")

        return render(request,'booking.html',context)

class Hire(View):
    def get(self,request,*args, **kwargs):
        context={}
        if not request.user.is_authenticated:
            messages.error(request,'pelase login to book your cleaner expert')
            return redirect('login')
        if request.session['city'] and request.session['date'] and request.session['slot']:
            print(args,kwargs)
            cleaner=CleanerProfile.objects.get(user__contact=int(kwargs['cleaneruser']))
            context['cleanerinfo']=cleaner      
            context['hiringmessage']="Hi! You're hiring to <u> {}</u>".format(cleaner.user.first_name)
            return render(request,'confirm_booking.html',context)
        else:
            messages.error(request,"pelase select city, date and slot time to book cleaner expert ")
            return redirect('newbooking')

    def post(self,request,*args, **kwargs):
        context={}
        if not request.user.is_authenticated:
            messages.error(request,'pelase login to book your cleaner expert')
            return redirect('login')
        if request.session['city'] and request.session['date'] and request.session['slot']:
            
            cleaner=CleanerProfile.objects.get(user__contact=int(kwargs['cleaneruser']))
            if cleaner.working_city==(City.objects.get(name=request.session['city'])):
                bookingdata1=bookings.objects.filter(city=cleaner.working_city,timeslot=request.session['slot'],dateofcleaning=request.session['date'],cleaner_id=cleaner)  #all cleaner who working in selected city
                if(bookingdata1).exists():
                    messages.error(request,"cleaner not available at moment..!!")
                    return redirect('newbooking')
                else:
                    bookings.objects.create(
                        customer_id=request.user,
                        cleaner_id=cleaner,
                        city=City.objects.get(name=request.session['city']),
                        dateofcleaning=request.session['date'],
                        timeslot=request.session['slot'])
                    context['hiredmessage']="thanks for hiring <u>{}</u>".format(cleaner.user.first_name)
                    
                    messages.success(request,context['hiredmessage'])
                    return redirect('profile')
            else:
                messages.error(request,"this cleaner not available at your area..!!")
                return redirect('newbooking')
        else:
            messages.error(request,"pelase select city, date and slot time to book cleaner expert ")
            return redirect('newbooking')