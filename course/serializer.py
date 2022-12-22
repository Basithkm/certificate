from rest_framework import serializers
from .models import CourseCategory,Course
from main.functions import get_auto_id


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseCategory
        fields=[
            'id',
            'course_category_name',
            'designation'

        ]

        extra_kwargs={
            'auto_id':{'read_only':True},
        }

    def create(self, validated_data):
        course_category=CourseCategory.objects.create(
            **validated_data,
        auto_id=get_auto_id(CourseCategory),
        # creator=self.context['request'].user
        )
        return course_category

class CourseSerializer(serializers.ModelSerializer):
    # course_category=CourseCategorySerializer(read_only=True)
    course_category_name=serializers.CharField(source='course_category.course_category_name',read_only=True)
    class Meta:
        model=Course
        fields=[
            'id',
            'course_name',
            'duration',
            'course_category',
            'course_category_name'

        ]

        extra_kwargs={
            'auto_id':{'read_only':True}
        }

    def create(self, validated_data):
        course=Course.objects.create(
            **validated_data,
            auto_id=get_auto_id(Course),
            # creator=self.context['request'].user
        )
        return course

# class CourseViewSerializer(serializers.ModelSerializer):
#     course_category=CourseCategorySerializer(read_only=True)
#     class Meta:
#         model=Course
#         fields=[
#             'id',
#             'course_name',
#             'duration',
#             'course_category'

#         ]