from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, MyAdListView, CommentViewSet

ads_router = SimpleRouter()
comments_router = SimpleRouter()

ads_router.register("", AdViewSet, basename="Ad")
comments_router.register("", CommentViewSet, basename="Comment")

urlpatterns = [
    path("me/", MyAdListView.as_view()),
    path("", include(ads_router.urls)),
    path("<int:ad_pk>/comments/", include(comments_router.urls)),
]
