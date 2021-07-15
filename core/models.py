from django.db import models
from django.contrib.auth.models import User
import datetime as dt


'''
Class model that represent the course data
'''
class Course(models.Model):

    COURSE_TYPE_CHOICES = (
        ('B', 'BUSINESS'),
        ('E', 'ENGINEERING'),
        ('T', 'TECHNOLOGY'),
        ('A', 'ARTS'),
    )
    course_name = models.CharField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=1, choices=COURSE_TYPE_CHOICES, null=True, default='B')


    def __str__(self):
        return self.course_name

class Student(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=50)
    student_email  = models.EmailField(max_length=70,blank=True,unique=True)
    adm_number = models.PositiveIntegerField(null =True,blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    applied_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        '''
        Display for student name
        '''
        return str('%s %s' % (self.first_name, self.last_name))


