from django.urls import path
from .views import students_list, student_detail, students_table

urlpatterns = [
    path('', students_list),  # JSON список студентов
    path('<int:student_id>/', student_detail),  # JSON один студент
]
