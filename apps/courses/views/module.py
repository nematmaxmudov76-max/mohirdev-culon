from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from apps.courses.models import Module
from apps.courses.serializers.module import ModuleSerializer

class ModuleListAPIView(ListAPIView):
    queryset = Module.objects.all().order_by("created_at")
    serializer_class = ModuleSerializer

class ModuleDetailAPIView(RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    lookup_field = "id"

class ModuleCreateAPIView(CreateAPIView):
    queryset = Module.objects.all().order_by("name")
    serializer_class = ModuleSerializer

class ModuleUpdateAPIView(UpdateAPIView):   
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    lookup_field = "id"

class ModuleDestroyAPIView(DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    lookup_field = "id"