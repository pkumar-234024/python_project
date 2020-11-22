from django import forms
from .models import *

class Student1Form(forms.ModelForm):
    class Meta:
        model = Student_first_year
        fields = "__all__"# ("sstudent_name", "srollno")

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student_second_year
        fields = "__all__"

class Student3Form(forms.ModelForm):
    class Meta:
        model = Student_third_year
        fields = "__all__"

class Student4Form(forms.ModelForm):
    class Meta:
        model = Student_fourth_year
        fields = "__all__"

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher_data
        fields = "__all__"