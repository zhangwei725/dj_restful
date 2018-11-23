# 核心功能  将模型转化json数据
from rest_framework import serializers

from main.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('image', 'id', 'type_name', 'name')
