from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_id', 'first_name', 'last_name', 'date_of_birth', 'enrollment_date']