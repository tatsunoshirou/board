from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    name = models.CharField('名前', max_length=32, blank=False)
    message = models.TextField('メッセージ', max_length=140)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "post"
        verbose_name = verbose_name_plural = "投稿"


class Good(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "good"
        verbose_name = verbose_name_plural = "いいね"



