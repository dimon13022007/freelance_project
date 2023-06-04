

from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),

    path('registr/', views.regist),

    path('advertisement/', views.advertisement),
    path('posts/', views.posts),
    path('payment/', views.payment_view),
    path('successful/', views.payment_successful),
    path('contacts/', views.contacts),




]
