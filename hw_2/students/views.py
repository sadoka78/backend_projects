from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Student

def students_list(request):
    # students = list(Student.objects.values())
    # return JsonResponse(students, safe=False)
    students = Student.objects.all()
    return render(request, 'studentss/student.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return JsonResponse({
        "id": student.id,
        "name": student.name,
        "surname": student.surname,
        "major": student.major,
        "year_of_study": student.year_of_study,
        "faculty": student.faculty,
    })

def students_table(request):
    students = Student.objects.all()
    return render(request, 'studentss/students_list.html', {'students': students})
