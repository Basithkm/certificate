from . import views
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('student',views.StudentViewset)
router.register('student_course',views.StudentCourseViewset)

urlpatterns = router.urls

