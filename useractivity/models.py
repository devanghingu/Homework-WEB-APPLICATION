from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin

class User(AbstractUser):
    username=models.CharField(max_length=50,blank=True)
    contact = models.CharField(max_length=12,unique=True, help_text="Your Contact number must be in numbers")
    address = models.CharField(max_length=1024,blank=True,null=True)
    pincode = models.IntegerField(null=True,blank=True) 
    is_cleaner=models.BooleanField(default=False,null=True,blank=True)
    USERNAME_FIELD = 'contact'
    REQUIRED_FIELDS = ['username']
    # USERNAME_REQUIRED = False
    # AUTHENTICATION_METHOD = "contact"
    def __str__(self):
        return str(self.contact)
class City(models.Model):
    """ Admin can add No. city where we provide service """
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)
class CleanerProfile(models.Model):
    """ When you want to be cleaner we just add some information """
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    quality_score=models.IntegerField(default=0)
    total_completed_job=models.IntegerField(default=0)
    working_city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True) #When CITY removed(it'll be null), cleaner need to work/add New city  
    working_time_slot=models.CharField(null=True,blank=True,max_length=50) # for future purpose

    def __str__(self):
        return str(self.user)
