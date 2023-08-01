from rest_framework import serializers
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source="id")
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id", read_only=True)
    author_image = serializers.ImageField(source="author.image", read_only=True, allow_empty_file=True)
    ad_id = serializers.ReadOnlyField(source="ad.id")
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        exclude = ["id", "author", "ad"]
        extra_fields = ["pk", "author_first_name", "author_last_name", "author_id", "author_image", "ad_id"]


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
