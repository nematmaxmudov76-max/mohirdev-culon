from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.interactions.models import Enrollment
from apps.interactions.serializers import EnrollmentSerializer

class EnrollmentListAPIView(ListAPIView):
    queryset = Enrollment.objects.all().

