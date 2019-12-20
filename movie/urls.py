from django.urls import path, include
from .import views


urlpatterns = [
    path('details/', views.movie, name='movie'),
    path('event_details', views.event, name='event')
    

]
