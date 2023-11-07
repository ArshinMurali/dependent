from . import views
from django.urls import path


urlpatterns = [

    path('',views.Main, name='main'),
    path('login/',views.Login, name='login'),
]
