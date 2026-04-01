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
    queryset = Enrollment.objects.all().order_by("-started_at")
    serializer_class = EnrollmentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class EnrollmentDetailAPIView(RetrieveAPIView): 
    queryset  = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

class EnrollmentCreateAPIView(CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class EnrollmentDeletedAPIView(DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

class EnrollmentUpdateAPIView(UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

