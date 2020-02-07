from django.urls import path
from . import views
urlpatterns = [
    path('newbooking',views.Newbooking.as_view(),name="newbooking"),
    path('hire/<int:cleaneruser>',views.Hire.as_view(),name='hire'),
]