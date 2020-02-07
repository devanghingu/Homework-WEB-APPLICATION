from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login as userlogin,logout as userlogout
from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.contrib import messages
from .forms import Loginform, signupform, CleanerForm
from .models import User,CleanerProfile
from booking.models import bookings
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate 
# Create your views here.
class login(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
           return redirect('index') 
        form=Loginform()
        return render(request,'login.html',{'form':form,'title':'Sign in'})
    def post(self,request,*args, **kwargs):
        if request.user.is_authenticated:
           return redirect('index') 
        form=Loginform(data=request.POST)
        if (form.is_valid()):
            contact=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user=authenticate(contact=contact,password=password)
            if user is not None:
                print('user fatchng code-------------')
                userlogin(request,user)
                request.user=user
                messages.success(request,"Login Success")
                return redirect('profile')
            else:
                messages.error(request,"Envalid username and password")
        else:
            print(form.errors)
            messages.error(request,"Envalid username and password")
        return render(request,'login.html',{'form':form,'title':'Sign in'})

class signup(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
           return redirect('index')
        form=signupform()
        return render(request,'signup.html',{'form':form})
    def post(self,request,*args, **kwargs):
        if request.user.is_authenticated:
           return redirect('index')
        form=signupform(request.POST)
        print(form.is_valid())
        if (form.is_valid()):
            form.save()
            print('success')
            messages.success(request,"registration done")
            return redirect('login')
        return render(request,'signup.html',{'form':form})

class logout(View):
    def get(self,request,*args, **kwargs):
        userlogout(request)
        return redirect('login')
    def post(self,request,*args, **kwargs):
        userlogout(request)
        return redirect('login')
class profile(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            context={}
            user=User.objects.get(contact=request.user)
            context['userdata']=user
            allbooking=bookings.objects.filter(customer_id=user)
            context['allbookings']=allbooking
            if(user.is_cleaner):
                cleanerprofile=CleanerProfile.objects.get(user=user)
                customerbooking=bookings.objects.filter(cleaner_id=cleanerprofile)
                context['cleanerprofile']=cleanerprofile
                context['customerbooking']=customerbooking
            return render(request,'user_profile.html',context)
        
        else:
            messages.error(request,'you must have to logged in')
            return redirect('login')

    def post(self,request,*args, **kwargs):
        pass
class BecomeCleaner(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            user=User.objects.get(contact=request.user)
            if user.is_cleaner ==False:
                form=CleanerForm(initial={'address':user.address})
                return render(request,'become_seller.html',{'form':form,'title':'Become Cleaner'})
            else:
                messages.info(request,"you're already cleaner expert")
                return redirect('profile')
        else:
            messages.INFO(request,"You must have to login before Apply")
            return redirect(login)
    def post(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            user=User.objects.get(contact=request.user)
            form=CleanerForm(data=request.POST)
            if user.is_cleaner==False :
                if form.is_valid():
                    user.address=form.cleaned_data['address']
                    user.pincode=form.cleaned_data['pincode']
                    user.is_cleaner=True
                    
                    cleaner_profile=CleanerProfile.objects.create(user=user)
                    cleaner_profile.working_city=form.cleaned_data['city']

                    cleaner_profile.save()
                    user.save()
                    messages.success(request,'you have been successfully applied')
                    return redirect('profile')
                else:
                    messages.error(request,"there are some error in input. check errors")
                    return render(request,'become_seller.html',{'form':form,'title':'Become Cleaner'})

            else:
                return redirect('profile')
        else:
            messages.INFO(request,"You must have to login before Apply")
            return redirect(login)

