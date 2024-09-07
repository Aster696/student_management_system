from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('add-student/', views.add_student, name='add-student'),
    path('edit-student/<str: strudent_id>', views.add_student, name='add-student'),
    path('post-student/', views.postStudent, name='post-student'),
    path('post-student/<str: strudent_id>', views.putStudent, name='put-student'),
]