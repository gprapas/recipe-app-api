from django.urls import path, include
from rest_framework import routers

from recipe.views import *

router = routers.DefaultRouter()

router.register(r'recipes', RecipeViewSet)
router.register('tags', TagViewSet)

app_name = 'recipe'

urlpatterns = router.urls

