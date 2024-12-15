from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'news-detail', NewsDetailViewSet)
router.register(r'home-p1', HomePageP1ViewSet)
router.register(r'city', CityViewSet)
router.register(r'state', StateViewSet)
router.register(r'category', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls))
]