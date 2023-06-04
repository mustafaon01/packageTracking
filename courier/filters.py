import django_filters
from .models import Package


class Package_filter(django_filters.FilterSet):
    package_id = django_filters.CharFilter(field_name="package_id", label="Package ID")


class Courier_filter(django_filters.FilterSet):
    courier_id = django_filters.CharFilter(field_name="courier_id", label="Courier ID")

