from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    cource_code = models.CharField(max_length=10, unique=True)
    cource_name = models.CharField(max_length=100)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='courses')

    def __str__(self) -> str:
        return self.cource_name