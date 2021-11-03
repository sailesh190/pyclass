"""pyclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from student import views
from student_api.views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"student", StudentViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexPage, name='index'),
    path('student/', views.StudentPage, name='student'),
    path('student/add/', views.AddStudentPage, name='add_student'),
    path('student/edit/<id>', views.EditStudentPage, name='edit_student'),
    path('student/delete/<id>', views.DeleteStudentPage, name='delete_student'),
    path('major/', views.MajorPage, name='major'),
    path('major/add/', views.AddMajorPage, name='add_major'),
    path('major/edit/<id>', views.EditMajorPage, name='edit_major'),
    path('major/delete/<id>', views.DeleteMajorPage, name='delete_major'),
    path('testget/', views.GetTestApi),
    path('testpost/', views.PostTestApi),
    path('api/', include(router.urls))
]
