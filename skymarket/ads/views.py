from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.filters import AdFilterSet
from ads.serializers import AdSerializer, AdDetailSerializer, AdCreateSerializer, CommentSerializer
from ads.permissions import IsAdmin, IsOwner


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

    default_permissions = [IsOwner | IsAdmin]
    permissions = {
        'list': [AllowAny],
        'retrieve': [IsAuthenticated],
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_queryset(self):
        return self.querysets.get(self.action, self.queryset)

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permissions)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class MyAdListView(ListAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    default_permissions = [IsOwner | IsAdmin]
    permissions = {
        'list': [AllowAny],
        'retrieve': [IsAuthenticated],
    }

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_pk']).select_related("author", "ad")

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permissions)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.kwargs['ad_pk'])
        return super().perform_create(serializer)
