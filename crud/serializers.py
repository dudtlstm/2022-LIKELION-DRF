from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User #장고의 기본 모델 불러 오기

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'content', 'created_at', 'update_at')

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'movie', 'content', 'created_at', 'update_at')

# 회원가입
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]

    def create(self, validated_data):
        user = User.objects.create(username = validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user