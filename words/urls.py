from django.urls import path, include

from rest_framework.routers import DefaultRouter

from words import views

router = DefaultRouter()
router.register('words', views.WordViewSet)

app_name = 'words'

urlpatterns = [
    path('', include(router.urls)),
]
