from .country_region import (
    CountryListCreateAPIView,
    CountryRetrieveUpdateDestroyAPIView,
    CountryRetrieveAPIView,
    RegionCreateAPIView,
    RegionListAPIView,
    RegionDeleteAPIView,
    RegionRetrieveAPIView,
    RegionUpdateAPIView,
)


from .file_upload import FileUploadAPIView
from .test_task import TestTaskAPIView
__all__ = [
    "CountryListCreateAPIView",
    "CountryRetrieveUpdateDestroyAPIView",
    "CountryRetrieveAPIView",
    "FileUploadAPIView",
    "RegionCreateAPIView",
    "RegionListAPIView",
    "RegionDeleteAPIView",
    "RegionRetrieveAPIView",
    "RegionUpdateAPIView",
    "TestTaskAPIView",
]