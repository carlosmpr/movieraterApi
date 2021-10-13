
from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, RatingViewSet
router = DefaultRouter()
router.register(r'movies',MovieViewSet)
router.register(r'rating',RatingViewSet)
urlpatterns = [
    path('', include(router.urls)),
]