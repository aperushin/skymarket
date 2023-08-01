from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.serializers import AdSerializer, AdDetailSerializer, AdCreateSerializer


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

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_queryset(self):
        return self.querysets.get(self.action, self.queryset)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class CommentViewSet(ModelViewSet):
    pass
