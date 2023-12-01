from django.urls import path, include
from rest_framework import routers

from recipe.views import *

router = routers.DefaultRouter()

router.register(r'recipes', RecipeViewSet)

urlpatterns = router.urls

