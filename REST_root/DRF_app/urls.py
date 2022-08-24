from django.urls import path
from . import views


urlpatterns=[
    path('Employee_cr/',views.Employee_CR.as_view(),name='Employee_cr'),
    path('Employee_rud/<pk>',views.Employee_RUD.as_view(),name='Employee_rud')
]
