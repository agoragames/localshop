from localshop.apps.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'releases/local', views.LocalReleasesViewset)

urlpatterns = router.urls
