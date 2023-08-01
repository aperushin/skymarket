from rest_framework import serializers
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source="id")

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source="id")
    phone = serializers.CharField(source="author.phone")
    author_first_name = serializers.CharField(source="author.first_name")
    author_last_name = serializers.CharField(source="author.last_name")
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        exclude = ["id", "author", "created_at"]
        extra_fields = ["pk", "phone", "author_first_name", "author_last_name", "author_id"]


class AdCreateSerializer(AdSerializer):
    def to_representation(self, instance):
        serializer = AdDetailSerializer(instance)
        return serializer.data
