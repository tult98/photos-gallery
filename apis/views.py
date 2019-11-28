from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from photos.models import Photo
from .serializers import PhotoDetailSerialize, PhotoListSeriaLize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class PhotoList(APIView):
    
    def get(self, request, page, format=None):
        photos_list = Photo.objects.all()
        paginator = Paginator(photos_list, 30)
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
        serializer = PhotoListSeriaLize(photos, many=True)
        return Response({"message": "Success", "photos": serializer.data})

    def post(self, request, format=None):
        serializer = PhotoDetailSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "photo": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PhotoDetail(APIView):
    
    def get(self, request, pk, format=None):
        try:
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoDetailSerialize(photo)
            return Response({"message": "Success", "photo": serializer.data})
        except Photo.DoesNotExist:
            return Response({"message": "The photo with that id doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoDetailSerialize(photo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Success", "photo": serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Photo.DoesNotExist:
            return Response({"message": "The photo with that id doesn't exist"}, status=status.HTTP_404_NOT_FOUND) 
    
    def delete(self, request, pk, format=None):
        try:
            photo = Photo.objects.get(pk=pk)
            photo.delete()
            return Response({"message": "Success"})
        except Photo.DoesNotExist:
            return Response({"message": "The photo with that id doesn't exist"}, status=status.HTTP_404_NOT_FOUND) 