from django.db.models import signals
from useractivity.models import User, CleanerProfile
from django.dispatch import receiver
from .models import bookings
from HomeCleaning_Homework.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


@receiver(signals.post_save,sender=bookings)
def test_signal(sender,instance,created,*args, **kwargs):
    print('hello',instance)
    to=instance.cleaner_id.user.email
    print('email sent to =',to)
    
    message="""
        you received orders from {}.
        order ID        : {}
        user contact    :   {}
        for more details goto your profile section 
    """.format(instance.customer_id.first_name,instance.id, instance.customer_id.contact)
    send_mail('Great news!!',message, EMAIL_HOST_USER, [str(to)], fail_silently = False)