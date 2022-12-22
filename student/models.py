from django.db import models
from course.models import Course
from django.utils.translation import gettext as _



from main.models import BaseModel



# Create your models here.

class Student(BaseModel):
    full_name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)
    # date_joined=models.DateTimeField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    # image=models.ImageField(null=True,blank=True)

    
    def __str__(self):
        return str(self.full_name)

    
    



class StudentCourse(BaseModel):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    progress=models.TextField(null=True,blank=True)


    
    class Meta:
        db_table = 'student_course'
        verbose_name =  _('Student_course')
        verbose_name_plural = _('Student_courses')
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.full_name)












