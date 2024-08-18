from django.db import models
from students.models import Students
from courses.models import Courses

# Create your models here.
class Enrollments(models.Model):
    student = models.IntegerField()
    course = models.IntegerField()
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f'{self.student} enrolled in {self.course}'