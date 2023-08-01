from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, MyAdListView, CommentViewSet

router = SimpleRouter()
router.register("", AdViewSet)
# router.register("<int:user_pk>", CommentViewSet)

urlpatterns = [
    path("me/", MyAdListView.as_view()),
    path("", include(router.urls))
]
