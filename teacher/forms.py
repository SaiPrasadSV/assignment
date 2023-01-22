from .models import *
from django import forms

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
        widgets={
                   "first_name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "last_name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "phone":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "email":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "room_number":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                }  


class SubjectForm(forms.ModelForm):
    class Meta:
        model = SubjectDetails
        fields = '__all__'
        widgets={
                   "teacher":forms.Select(attrs={'class': "form-control form-control-sm"}),
                   "subject_name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                }  

class FileForm(forms.Form):
    teacher_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': "form-control form-control-sm"}))
    teacher_images = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': "form-control form-control-sm"}))