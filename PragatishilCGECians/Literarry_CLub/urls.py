from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('main_page/', views.main_page),
    path('register/', views.register),
    path('peptalks/',views.peptalks),
    path('peptalksregister/',views.peptalksregister),
    path('Arietta_Home_Page/',views.Arietta_Home_Page),
    path('Arietta_Register/',views.Arietta_Register),
    path('Debate_Home_Page/',views.Debate_Home_Page),
    path('Debate_Register/',views.Debate_Register),
    path('Literarry_Home_Page/',views.Literarry_Home_Page),
    path('Literarry_Register/',views.Literarry_Register),
    path('Pratibimba_Home_Page/',views.Pratibimba_Home_Page),
    path('Pratibimba_Register/',views.Pratibimba_Register),
    path('Rongmilanti_Home_Page/',views.Rongmilanti_Home_Page),
    path('Rongmilanti_Register/',views.Rongmilanti_Register),
    path('Techonics_Home_Page/',views.Techonics_Home_Page),
    path('Techonics_Register/',views.Techonics_Register),
    
]
