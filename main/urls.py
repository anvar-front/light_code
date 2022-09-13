from django.urls import path
from main import views

urlpatterns = [
    path('employee', views.EmployeeAPIView.as_view()),
    path('machine', views.MachineAPIView.as_view()),
    path('work', views.WorkAPIView.as_view())
]
