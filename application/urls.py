from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home),
    path('register',views.register),
    path('display',views.display),
    path('login',views.addlogin),
    path('logout',views.logout),
    path('news',views.news),
    path('about',views.about),
    path('contact',views.contact),


    path('honda',views.honda),
    path('hondajazz',views.hondajazz),
    path('hondaamaze',views.hondaamaze),
    path('hondabrio',views.hondabrio),
    path('hondacity',views.hondacity),

    path('maruti',views.maruti),
    path('alto',views.alto),
    path('ritz',views.ritz),
    path('swift',views.swift),
    path('wagnor',views.wagnor),

    path('toyota',views.toyota),
    path('liva',views.liva),
    path('innova',views.innova),
    path('fortuner',views.fortuner),
    path('landcruiser',views.landcruiser),

    path('hyundai',views.hyundai),
    path('creta',views.creta),
    path('i10',views.i10),
    path('i20',views.i20),
    path('venue',views.venue),
]
