from django.forms import ModelForm
from student import models


class StudentForm(ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"
        exclude = ["id"]
        
class MajorForm(ModelForm):
    class Meta:
        model = models.Major
        fields = "__all__"
        exclude = ["id"]