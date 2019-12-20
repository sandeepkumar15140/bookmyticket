from django.urls import path, include
from .import views


urlpatterns = [
    path('details/', views.movie, name='movie'),
    

]
