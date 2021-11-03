from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from student import models
from student import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def IndexPage(request):
    data = {"msg": "Hey, how are you doing this {}?".format(datetime.now().strftime("%A"))}
    #data = {"major": models.Major.objects.all().values("name")} 
    return render(request, "index.html", data)

def StudentPage(request):
    data = {"student": models.Student.objects.all().values("id", "name", "email", "sex", "major_id__name")} 
    return render(request, "student.html", data)

def AddStudentPage(request):
    if request.method == "POST":
        form = forms.StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/student")
    else:
        form = forms.StudentForm()
        return render(request, "add_student.html", {"form": form})
    
def EditStudentPage(request, id):
    obj = get_object_or_404(models.Student, id = id)
    form = forms.StudentForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/student")
    else:
        return render(request, "edit_student.html", {"form": form})
    
def DeleteStudentPage(request, id):
    obj = get_object_or_404(models.Student, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect("/student")
    else:
        return render(request, "delete_student.html", {})

def MajorPage(request):
    data = {"major": models.Major.objects.all().values("id", "name")} 
    return render(request, "major.html", data)

def AddMajorPage(request):
    if request.method == "POST":
        form = forms.MajorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/major")
    else:
        form = forms.MajorForm()
        return render(request, "add_major.html", {"form": form})
    
def EditMajorPage(request, id):
    obj = get_object_or_404(models.Major, id = id)
    form = forms.MajorForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/major")
    else:
        return render(request, "edit_major.html", {"form": form})
    
def DeleteMajorPage(request, id):
    obj = get_object_or_404(models.Major, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect("/major")
    else:
        return render(request, "delete_major.html", {})
    
def GetTestApi(request):
    if request.method == "GET":
        get_data = request.GET.get("testdata")
        return JsonResponse({"foo": "GET", "mygetdata": get_data})

@csrf_exempt
def PostTestApi(request):
    if request.method == "POST":
        get_data = request.GET.get("testdata")
        post_get_data = json.loads(request.body)
        return JsonResponse({"foo": "GET", "mygetdata": get_data, "bodymsg": post_get_data})