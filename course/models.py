from django.db import models

from main.models import BaseModel




# Create your models here.


class CourseCategory(BaseModel):
    
    course_category_name=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)

    
    def __str__(self):
        return str(self.course_category_name)





class Course(BaseModel):
    course_name=models.CharField(max_length=50,null=True,blank=True)
    duration=models.CharField(max_length=255,null=True,blank=True)
    course_category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.course_name)

