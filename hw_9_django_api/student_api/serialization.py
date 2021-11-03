from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    major = serializers.ReadOnlyField(source="major.name")
    class Meta:
        model = Student
        fields = ("id", "name", "email", "sex", "major")