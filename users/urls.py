from django.urls import path, include
from rest_framework import routers
from .views import UserView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users', UserView.as_view()),
]
