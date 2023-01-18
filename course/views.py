from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Course,CourseCategory
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from .serializer import CourseCategorySerializer,CourseSerializer
from .pagination import DefaultPagination



# Create your views here.

class CourseCategaryViewset(ModelViewSet):
    queryset=CourseCategory.objects.filter(is_deleted=False)
    serializer_class=CourseCategorySerializer
    pagination_class=DefaultPagination
    

    
class CourseViewset(ModelViewSet):
    queryset=Course.objects.filter(is_deleted=False).select_related('course_category')
    serializer_class=CourseSerializer
    pagination_class=DefaultPagination

