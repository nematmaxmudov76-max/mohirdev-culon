from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView
)

from apps.common.serializers import  CountrySerializer
from apps.common.models import Country, Region

# COUNTRY VIEWS

class CountryListCreateAPIView(ListCreateAPIView):
    queryset = Country.objects.all().order_by("name")
    serializer_class = CountrySerializer


class CountryRetrieveUpdateDestroyAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryRetrieveAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"


# REGION VIEWS

class RegionListCreateAPIView(ListCreateAPIView):
    queryset = Region.objects.all().order_by("name")
    serializer_class = CountrySerializer


class RegionDestroyAPIView(DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"

class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"