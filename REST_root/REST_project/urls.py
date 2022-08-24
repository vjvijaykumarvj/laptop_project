from django.urls import path,include

urlpatterns = [
    #http://127.0.0.1:8000/Employee/Employee_cr/
    path('Employee/',include('DRF_app.urls'))
]
