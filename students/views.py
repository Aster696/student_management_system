from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Students
from .forms import StudentForm

# Create your views here.
def student_list(request):
    students = Students.objects.all()
    return render(request, 'students/student_list.html', {'data': students})

def add_student(request):
    return render(request, 'students/add_student.html')

def postStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        try:
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student-list')
        except Exception as e:
                messages.error(request, f'Error: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else: 
        form = StudentForm()
    
    return render(request, 'students/add_student.html', {'form': form})