from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.models import Course, Student


# class StudentPostForm(forms.ModelForm):
#     '''
#     Class to create a form for an authenticated user to creat acertificate application
#     '''
#     class Meta:
#         model = Student
#         fields = ['__all__']

class StudentForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to creat acertificate application
    '''
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'adm_number', 'student_email', 'course']

class CourseForm(forms.ModelForm):
    '''
    class that creates the course form
    '''
    class Meta:
        model = Course
        fields = ['course_name']

