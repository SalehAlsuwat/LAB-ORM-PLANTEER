from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.log_out, name='log_out'),

]