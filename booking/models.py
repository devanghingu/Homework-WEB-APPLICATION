from django.db import models
from useractivity.models import User,CleanerProfile,City
# Create your models here.
class bookings(models.Model):
    CHOICES=(
        (1,'10 AM - 12 PM'),
        (2,'12 PM - 02 PM'),
        (3,'02 PM - 04 PM'),
        (4,'04 PM - 06 PM'),
        (5,'06 PM - 08 PM')
    )
    customer_id=models.ForeignKey(User, on_delete=models.PROTECT)
    cleaner_id=models.ForeignKey(CleanerProfile, on_delete=models.PROTECT)
    city=models.ForeignKey(City, on_delete=models.PROTECT)
    address=models.TextField(verbose_name='Address',null=True,blank=True) 
    dateofcleaning=models.DateField(verbose_name="Date Of Cleaning")
    timeslot=models.IntegerField(choices=CHOICES)
    notes=models.TextField(verbose_name='any message to cleaner ',null=True,blank=True)
    job_complated=models.BooleanField(verbose_name="job Completed",default=False)

    def __str__(self):
        data=["ID:[",str(self.id), "]--CITY : [ ", str(self.city) ,' ] Date : [', str(self.dateofcleaning) , '] time : ' , str(self.timeslot)]
        data="user : {}, [Cleaner : {} ] , city : {}, date : {}, slot: {} ".format(self.customer_id,self.cleaner_id,self.city,self.dateofcleaning,self.timeslot)
        return str(data)