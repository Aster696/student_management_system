from django.shortcuts import render
from .models import Students

# Create your views here.
def student_list(request):
    students = Students.objects.all()
    return render(request, 'students/student_list.html', {'data': students})

def add_student(request):
    return render(request, 'students/add_student.html')