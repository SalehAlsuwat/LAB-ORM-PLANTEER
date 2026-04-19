from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('contact/messages/', views.messages_view, name='messages_view'),

]