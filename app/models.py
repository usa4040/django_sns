from accounts.models import CustomUser
from django.db import models


# Create your models here.
class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
