from django.contrib import admin
from .models import User,City,CleanerProfile
# Register your models here.
admin.site.register(User)
admin.site.register(City)
admin.site.register(CleanerProfile)