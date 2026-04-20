from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.common.tasks import task

class TestTaskAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        task.delay()
        return Response({"message":"task ishga tushdi"})


