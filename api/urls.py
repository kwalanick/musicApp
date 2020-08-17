from django.urls import path , include
from rest_framework import routers
from .views import UserViewSet , SongViewSet ,FileUploadView


router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('songs',SongViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('artists/', FileUploadView.as_view()),
]