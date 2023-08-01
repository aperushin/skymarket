from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet

router = SimpleRouter()
router.register("ads", AdViewSet)

urlpatterns = [

]

urlpatterns += router.urls
