from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Course, Student
from .forms import CourseForm, StudentForm

def index(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        raise Http404("No course found")
    return render(request, 'courses.html', {'courses': courses})
    

def new_application(request):
    '''
    View function to display a form for creating a post to a logged in authenticated user
    '''
    current_user = request.user

    if request.method == 'POST':

        form = StudentForm(request.POST, request.FILES)

        if form.is_valid:
            application = form.save(commit=False)
            application.user = current_user
            application.save()
            return redirect(index)
    else:
        form = StudentForm()
    return render(request, 'apply_cert.html', {"form":form})



def reports(request):
    labels = []
    data = []

    queryset = Student.objects.order_by('id')
    students = {
        'pending approvals': queryset.filter(is_approved=False).count(),
        'approved': queryset.filter(is_approved=True).count()
    }
    
    for k in students:
        labels.append("name")
        data.append(3)

    return render(request, 'reports.html', {
        'labels': labels,
        'data': data,
    })
