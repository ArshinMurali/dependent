from . import views
from django.urls import path

urlpatterns = [

    path('form', views.dependantfield, name='dependantfield'),
    path('get-states/', views.get_states, name='get_states'),
    path('last', views.last, name='last'),

]
