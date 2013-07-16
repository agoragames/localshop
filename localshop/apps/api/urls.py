from django.conf.urls.defaults import patterns, url

from localshop.apps.api import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'local_releases', views.LocalReleasesViewset)

urlpatterns = router.urls
