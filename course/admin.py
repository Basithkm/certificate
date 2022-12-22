from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=(
          
            'course_name',
            'duration',
            'course_category'

    )
admin.site.register(Course,CourseAdmin)


class CourseCategoryAdmin(admin.ModelAdmin):
    list_display=(
            
            'course_category_name',
            'designation'

        
    )
admin.site.register(CourseCategory,CourseCategoryAdmin)