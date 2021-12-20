from django.urls import path
from .views import registerView,loginView,logoutView

urlpatterns=[
    path('register/',registerView,name='registerPage'),
    path('login/',loginView,name='loginPage'),
    path('logout/',logoutView,name='logoutPage')
]