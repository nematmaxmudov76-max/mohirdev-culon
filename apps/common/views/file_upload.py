from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from apps.common.serializers import FileUploadSerializer
from apps.common.models import Media

class FileUploadAPIView(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes  = [FormParser, MultiPartParser]

    @extend_schema(request={"multipart/form-data": FileUploadSerializer})
    def post(self, request, *args, **kwargs):
        file = request.data.get("file")
        request.data["file"] = file

        if file.size > 5 * 1024 * 1024:
            raise ValidationError({"file": "file 5 mb dan oshib ketdi"})

        if file.content_type not in [
            "image/jpeg",
            "image/png",
            "image/gif",
        ]:
            raise ValidationError({"file": "file image tip da bo'lish kerak"})

        return super().post(request, *args, **kwargs)
