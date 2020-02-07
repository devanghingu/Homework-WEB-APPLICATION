from django.urls import path
from . import views
urlpatterns = [

    path('login/',views.login.as_view(),name="login"),
    path('signup/',views.signup.as_view(),name="signup"),
    path('logout/',views.logout.as_view(),name="logout"),
    # path('profile/',views.profile.as_view(),name="profile"),
    path('profile/',views.profile.as_view(),name='profile'),
    path('become_cleaner',views.BecomeCleaner.as_view(),name='becomecleaner'),
    # path('profile/edit',views.profile.as_view(),name="profile"),

]