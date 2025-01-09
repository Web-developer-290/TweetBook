from django.urls import path
from . import views

urlpatterns = [

    path('', views.tweet_list, name="tweet_list"),
    path('about/', views.About, name="About"),
    path('Contact_Us', views.contactus, name="contactus"),
    path('create/', views.create, name="create"),
    path('<int:tweet_id>/edit/', views.edit, name="edit"),
    path('<int:tweet_id>/delete/', views.delete, name="delete"),
    path('register/', views.register, name="register"),
    path('search/', views.searchbar, name='search'),
    
]