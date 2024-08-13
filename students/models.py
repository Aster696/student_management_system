from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'