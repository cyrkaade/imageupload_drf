from rest_framework import serializers
from .models import UploadImage

# Creating Serializer for UploadImage

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('pk', 'original', 'small', 'medium', 'expiring_image_url', 'expire_secs_only_for_enterprise')
        read_only_fields = ['small', 'medium', 'expiring_image_url',]
    
    

 
        

    
