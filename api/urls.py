from django.urls import path
from .views import CarBrandAPIView, CarAPIView, CarBrandDetailAPIView, CarDetailAPIView

urlpatterns=[
path('brands/', CarBrandAPIView.as_view()),
path('brands/<int:pk>/', CarBrandDetailAPIView.as_view()),
path('cars/', CarAPIView.as_view()),
path('cars/<int:brand_id>/', CarAPIView.as_view()),
path('cars/<int:pk>/', CarDetailAPIView.as_view()),
]