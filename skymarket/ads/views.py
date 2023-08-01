from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ads.models import Ad, Comment
from ads.filters import AdFilterSet
from ads.serializers import AdSerializer, AdDetailSerializer, AdCreateSerializer, CommentSerializer


class AdPagination(PageNumberPagination):
    page_size = 4


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    querysets = {
        "retrieve": Ad.objects.select_related("author"),
    }
    default_serializer = AdSerializer
    serializer_classes = {
        "retrieve": AdDetailSerializer,
        "create": AdCreateSerializer,
        "partial_update": AdCreateSerializer,
    }
    pagination_class = AdPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilterSet

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_queryset(self):
        return self.querysets.get(self.action, self.queryset)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class MyAdListView(ListAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_pk']).select_related("author", "ad")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.kwargs['ad_pk'])
        return super().perform_create(serializer)
