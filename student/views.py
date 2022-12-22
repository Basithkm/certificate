from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import StudentSerializer,StudentCourseSerializer
from .pagination import DefaultPagination


# Create your views here.
class StudentViewset(ModelViewSet):
    queryset=Student.objects.filter(is_deleted=False)
    serializer_class=StudentSerializer
    pagination_class=DefaultPagination


class StudentCourseViewset(ModelViewSet):
    queryset=StudentCourse.objects.filter(is_deleted=False).select_related('student','course')
    serializer_class=StudentCourseSerializer
    pagination_class=DefaultPagination
