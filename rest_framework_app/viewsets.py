from rest_framework import viewsets
from rest_framework_app.serializers import UploadImageSerializer
from .models import UploadImage

# Creating viewsets

class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer


