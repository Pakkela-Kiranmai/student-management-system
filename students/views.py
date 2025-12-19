
from .models import Student, Attendance , Marks
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login



@login_required
def view_students(request):
    students = Student.objects.all()
    return render(request, 'students/view_students.html', {'students': students})



@login_required
def profile(request):
    return render(request, 'students/profile.html')



@login_required
def home(request):
    total_students = Student.objects.count()
    courses = Student.objects.values_list('course', flat=True).distinct()
    total_courses = len(courses)
    recent_students = Student.objects.order_by('-id')[:5]

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'recent_students': recent_students,
    }
    return render(request, 'students/home.html', context)


def add_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        roll_number = request.POST['roll_number']
        course = request.POST['course']

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            roll_number=roll_number,
            course=course
        )
        return redirect('view_students')

    return render(request, 'students/add_student.html')


def view_students(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'students/view_students.html', {'students': students})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.roll_number = request.POST['roll_number']
        student.course = request.POST['course']
        student.save()
        return redirect('view_students')
    messages.success(request, f"Student {student.first_name} {student.last_name} updated successfully!")

    return render(request, 'students/edit_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('view_students')
    messages.success(request, f"Student {student.first_name} {student.last_name} deleted successfully!")

    return render(request, 'students/delete_student.html', {'student': student})

def about(request):
    return render(request, 'students/about.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')
    return render(request, 'students/register.html')

def dashboard(request):
    return render(request, 'students/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'students/profile.html')

@login_required
def settings(request):
    return render(request, 'students/settings.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # 🔥 THIS CREATES SESSION
            return redirect('dashboard')
        else:
            return render(request, 'students/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'students/login.html')

@login_required
def attendance(request):
    students = Student.objects.all()

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(str(student.id))
            if status:
                Attendance.objects.create(
                    student=student,
                    status=status
                )
        return redirect('dashboard')

    return render(request, 'students/attendance.html', {
        'students': students
    })

@login_required
def add_marks(request):
    students = Student.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')

        student = Student.objects.get(id=student_id)

        Marks.objects.create(
            student=student,
            subject=subject,
            marks=marks
        )
        return redirect('view_marks')

    return render(request, 'students/add_marks.html', {
        'students': students
    })

@login_required
def view_marks(request):
    marks = Marks.objects.all()
    return render(request, 'students/view_marks.html', {
        'marks': marks
    })
