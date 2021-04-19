from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('home', views.index, name='home'),
    path('cancel', views.cancel, name='cancel'),
    path('book', views.book, name='book'),
    path('ticket', views.ticket, name='ticket'),
    path('contact', views.contact, name='contact'),
    path('cancelled', views.cancelled, name='cancelled'),
    path('popup', views.popup, name='popup')
]
