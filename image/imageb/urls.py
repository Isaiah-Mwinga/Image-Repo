from django.urls import path
from .views import ImageUploadAPIView
from . import views

urlpatterns = [
    path('upload/', ImageUploadAPIView.as_view(), name='image-upload'),
     path('upload/', views.upload_image, name='upload_image'),
    # Add other URL patterns as needed
]




