from django.contrib import admin
from student import models
# Register your models here.

@admin.register(models.Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ("name", "email", "sex", "major")
    list_display = ("id", "name", "email", "sex", "major")
    list_filter = ("major",)
    search_fields = ("email", "name")
    #exclude = ("phone",)