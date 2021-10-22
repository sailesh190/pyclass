from django.db import models

# Create your models here.

class City(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    # name_cn = models.CharField(max_length=50,blank=True,null=True)
    # key = models.CharField(max_length=22)
    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    # name_cn = models.CharField(max_length=50,blank=True,null=True)
    # key = models.CharField(max_length=22)
    def __str__(self):
        return f'{self.name},{self.email}'