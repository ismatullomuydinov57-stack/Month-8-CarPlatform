from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CarBrand, Car
from .serializer import CarBrandSerializer, CarSerializer


class CarBrandAPIView(ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarBrandDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarAPIView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        brand_id=self.kwargs.get("brand_id", None)
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")

        if brand_id:
            queryset=Car.objects.filter(brand_id=brand_id)
        else:
            queryset=Car.objects.all()
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

    lookup_field = 'pk'
    lookup_url_kwarg = 'brand_id'


class CarDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



