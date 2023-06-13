from django.db import models
from common.models import CommonModel


class Comment(CommonModel):
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    comment = models.TextField()
    imageUrl = models.TextField(blank=True)
    blogid = models.IntegerField()

    def __str__(self):
        return self.author.username