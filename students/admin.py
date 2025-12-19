from django.contrib import admin
from .models import Student
from .models import Attendance
from .models import Marks

admin.site.register(Marks)

admin.site.register(Attendance)

admin.site.register(Student)
