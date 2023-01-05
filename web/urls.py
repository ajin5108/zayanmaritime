from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('myaccount',views.myaccount,name="myaccount"),
    path('partner',views.partner,name="partner"),
    path('pricing',views.pricing,name="pricing"),
    path('privacy',views.privacy,name="privacy"),
    path('register',views.register,name="register"),
    path('requestquote',views.requestquote,name="requestquote"),
    path('servicedetails/<int:id>/',views.servicedetails,name="servicedetails"),
    path('services',views.services,name="services"),
    path('team',views.team,name="team"),
    path('termsandconditions',views.termsandconditions,name="termsandconditions"),
    path('testimonials',views.testimonials,name="testimonials"),
    path('gallery',views.gallery,name="gallery"),
    path('career',views.career,name="career"), 
    
    path('message/',views.message,name="message"),
    path('message2/',views.message2,name="message2"),    
    
]