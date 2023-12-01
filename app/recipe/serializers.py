"""Serializer for Recipe APIs"""
from rest_framework import serializers
from recipe.models import *


class RecipeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']