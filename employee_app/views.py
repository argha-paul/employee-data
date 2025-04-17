from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer
from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

def dashboard(request):
    return render(request, 'employee_app/dashboard.html')

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name','email','department__name']
    ordering_fields = ['hire_date','salary']

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

class AttendanceListView(generics.ListAPIView):
    queryset = Attendance.objects.select_related('employee').all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']