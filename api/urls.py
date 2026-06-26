from django.urls import path, include
from .views import CarAPIViewSet, CommentAPIViewSet, CarBrandAPIViewSet
from rest_framework.routers import SimpleRouter


router=SimpleRouter()
router.register('brands', CarBrandAPIViewSet, basename='carbrand')
router.register('cars', CarAPIViewSet, basename='car')
router.register('comments', CommentAPIViewSet)

urlpatterns=[
path('', include(router.urls)),
path('cars/brand/<int:brand_id>/', CarAPIViewSet.as_view({'get':'list'})),
path('cars/<int:car_id>/comments/', CommentAPIViewSet.as_view({'get':'list', 'post':'create'}))
]
