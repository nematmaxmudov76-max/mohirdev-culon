from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


from apps.accounts.models import Education
from apps.accounts.serializers.education import EducationSerializer

class EducationListAPIView(ListCreateAPIView):
    queryset = Education.objects.all().order_by("name")
    serializer_class = EducationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class EducationDetailAPIView(RetrieveAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id" # chunki id orqali olishni xohlaymiz

class EducationCreateAPIView(CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class EducationUpdateAPIView(UpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id" # chunki id orqali yangilashni xohlaymiz

class EducationDeleteAPIView(DestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id" # chunki id orqali o'chirishni xohlaymiz