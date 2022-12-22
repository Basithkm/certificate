from .import views
from rest_framework_nested import routers


router=routers.DefaultRouter()
router.register('course_category',views.CourseCategaryViewset)
router.register('course',views.CourseViewset)

urlpatterns = router.urls



