from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.

def HomePage(request):
    return render(request, 'app/home.html')

# -----------------------
def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'app/student_list.html',context)


def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully")
            return redirect('student_list')
        messages.error(request, "Validation failed")
    context = {
        'form': form
    }
    return render(request, 'app/student_add.html', context)
# ------------------------

def student_detail(request,id):
    student = Student.objects.get(id = id)
    print(student)
    context = {
        "student": student
    }
    return render(request, 'app/student_detail.html', context)

def student_update(request,pk):
    pass

def student_delete(request,pk):
    pass
