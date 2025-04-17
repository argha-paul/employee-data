from django.urls import path
from .views import EmployeeListCreateView, EmployeeDetailView, AttendanceListView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
]