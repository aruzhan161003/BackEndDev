from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register('api/students', views.StudentView)

urlpatterns = router.urls
