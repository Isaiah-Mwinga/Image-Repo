# views.py
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ImageUploadSerializer
from rest_framework.permissions import AllowAny

def upload_image(request):
    return render(request, 'upload_image.html')

class ImageUploadAPIView(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow any user to access this view

    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)

        if serializer.is_valid():
            image_yaml = serializer.validated_data['image']
            return Response({'image_yaml': image_yaml}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




