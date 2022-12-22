from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'full_name',
        'start_date',
        'end_date',
        'designation'

    )
admin.site.register(Student,StudentAdmin)


class StudentCourseAdmin(admin.ModelAdmin):
    list_display=(
                    'id',
            'student',
            'course',
            'progress',
            

    )
admin.site.register(StudentCourse,StudentCourseAdmin)



