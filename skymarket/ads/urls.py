from django.urls import path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, MyAdListView

router = SimpleRouter()
router.register("ads", AdViewSet)

urlpatterns = [
    path("ads/me/", MyAdListView.as_view())
]

urlpatterns += router.urls
