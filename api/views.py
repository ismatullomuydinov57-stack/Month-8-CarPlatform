from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CarBrand, Car, Comment
from .serializer import CarBrandSerializer, CarSerializer, CommentSerializer
from .permissions import MyIsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet


class CarBrandAPIViewSet(ModelViewSet):
    queryset = CarBrand.objects.all().prefetch_related('cars')
    serializer_class = CarBrandSerializer

class CarAPIViewSet(ModelViewSet):
    # queryset = Car.objects.all().select_related('brand').only('id', 'model_name', 'price', 'year', 'brand')
    queryset = Car.objects.all().select_related('brand').defer('color')
    serializer_class = CarSerializer

    def get_queryset(self):
        brand_id = self.kwargs.get("brand_id", None)
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")

        if brand_id:
            queryset = Car.objects.filter(brand_id=brand_id)
        else:
            queryset = Car.objects.all()
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

    lookup_field = 'pk'
    lookup_url_kwarg = 'brand_id'

class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [MyIsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data["user"]=self.request.user
        serializer.validated_data["car_id"]=self.kwargs.get("car_id")
        serializer.save()






