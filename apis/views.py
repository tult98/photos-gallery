from rest_framework import viewsets
from photos.models import Photo
from .serializers import PhotoSerialize

# Create your views here.

class PhotoAPIView(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerialize