from django_filters import rest_framework as filters

from ads.models import Ad


class AdFilterSet(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ("title", )
