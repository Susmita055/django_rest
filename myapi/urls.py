from django.urls import include, path
from .views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]