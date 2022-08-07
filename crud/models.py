from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #데이터베이스 상으로 확인해 보면 Movie의 id와 Review의 movie가 동일한 값을 가지게 될 것

#궁금한 점
#1. movie의 name을 받아 올 수 있는 방법이 있는 건가
#2. Review에 id 필드를 정의해 주지 않아도 뜨는 이유는 movie에서 id가 있기 때문인 건가