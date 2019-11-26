from rest_framework import serializers
from photos.models import Photo

class PhotoSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title', 'description', 'url', 'created_at', 'updated_at')


        
