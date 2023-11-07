from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('logins',views.logins,name='logins'),
    path('new',views.new,name='new'),
    # path('form',views.form,name='form'),
    # path('last',views.last,name='last'),
]