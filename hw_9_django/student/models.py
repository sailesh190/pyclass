from django.db import models

# Create your models here.

SEX_CHOICES = [("Female", "Female"), ("Male", "Male")]

class Major(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    sex = models.CharField(max_length=255, choices=SEX_CHOICES)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name