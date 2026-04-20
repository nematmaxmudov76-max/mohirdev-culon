from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from apps.common.serializers import  CountrySerializer, RegionSerializer
from apps.common.models import Country, Region

# COUNTRY VIEWS

class CountryListCreateAPIView(ListAPIView):
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

class RegionCreateAPIView(CreateAPIView):
    queryset = Region.objects.all().order_by("name")
    serializer_class = RegionSerializer

class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all().order_by("name")
    serializer_class = RegionSerializer

class RegionDeleteAPIView(DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = "id"

class RegionRetrieveAPIView(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = "id"

class RegionUpdateAPIView(UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = "id"