# 核心功能  将模型转化json数据
from rest_framework import serializers

from main.models import Film, CateLog


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class CateLogSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True, read_only=True)

    class Meta:
        model = CateLog
        fields = '__all__'
