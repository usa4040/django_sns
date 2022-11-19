from accounts.models import CustomUser
from django.db import models


# Create your models here.
class Post(models.Model):
    content = models.TextField()
    post_image = models.ImageField(upload_to='img/',null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(CustomUser, related_name='related_post', blank=True)

    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = ["-created_at"]


class LikeForPost(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)