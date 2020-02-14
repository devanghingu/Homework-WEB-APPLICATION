from django.shortcuts import render
from django.views import View
from useractivity. models import User

class index(View):
    def get(self,request,*args, **kwargs):
        return render(request,'index.html')