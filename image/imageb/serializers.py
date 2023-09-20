# serializers.py
import yaml
from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.FileField()

    def validate_image(self, value):
        # Ensure the uploaded file is an image (you can add more validation here)
        if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            raise serializers.ValidationError('Invalid image format')

        # Convert the image file to YAML
        try:
            image_data = value.read()
            image_yaml = yaml.dump({'image_data': image_data}, default_style='"')
        except Exception as e:
            raise serializers.ValidationError(f'Error converting image to YAML: {str(e)}')

        return image_yaml
