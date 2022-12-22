from rest_framework import serializers
from .models import Student,StudentCourse
from course.models import Course
from main.functions import get_auto_id
# from django.contrib.auth import user
# from django.template import  Context

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=[
            'id',
            'full_name',
            'email',
            'phone',
            # 'birth_date',
            'start_date',
            'end_date',
            'designation',
            # 'date_joined',
            'address',
            'dob'
            # 'image'

        ]

        extra_kwargs={
            'auto_id':{'read_only':True}
        }

    def create(self, validated_data):
        student=Student.objects.create(
            **validated_data,
            auto_id=get_auto_id(Student),
            # creator = self.context['request'].user
        )
        return  student



# class StudentCourseStudenDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields=[
#             'id',
#             'full_name',

#         ]

#         extra_kwargs={
#             'auto_id':{'read_only':True}
#         }

#     def create(self, validated_data):
#         course=Course.objects.create(
#             **validated_data,
#             auto_id=get_auto_id(Course),
            
#         )
#         return course


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Course
#         fields=[
#             'course_name',
#             'duration',
#             'course_category'

#         ]

class StudentCourseSerializer(serializers.ModelSerializer):
    # student=StudentCourseStudenDetailSerializer()
    # course=CourseSerializer(read_only=True)
    student_name=serializers.CharField(source='student.full_name',read_only=True)
    course_name=serializers.CharField(source='course.course_name',read_only=True)
    class Meta:
        model=StudentCourse
        fields=[
            'id',
            'student',
            'student_name',
            'course',
            'course_name',
            'progress',
            

        ]

        extra_kwargs={
            'auto_id':{'read_only':True}
        }

    def create(self, validated_data):
        student_course=StudentCourse.objects.create(
            **validated_data,
            auto_id=get_auto_id(StudentCourse),
            # creator = self.context['request'].user
        )
        return  student_course

        
