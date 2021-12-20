from django.urls import path
from .views import laptop_view,laptop_info,Data_update,Delete_data

urlpatterns=[
    path('add/',laptop_view.as_view(),name='addlaptop'),
    path('show/',laptop_info.as_view(),name='showlaptop'),
    path('update/<int:id>/',Data_update.as_view(),name='updatedata'),
    path('delete/<int:id>/',Delete_data.as_view(),name='deletedata')
]