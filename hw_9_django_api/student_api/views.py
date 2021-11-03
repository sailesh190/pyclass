from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from student_api.serialization import StudentSerializer
from student.models import Student
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]