from django.db import models
from common.models import CommonModel


class Blog(CommonModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("users.User", on_delete= models.CASCADE)
    content = models.TextField()
    hits = models.IntegerField()
    recoms = models.IntegerField()
    cate_no = models.ForeignKey("categories.Category", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Hit(CommonModel):
    category=models.ForeignKey("categories.Category", on_delete=models.CASCADE)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    userip = models.TextField(max_length=16)
    
class Recom(CommonModel):
    category=models.ForeignKey("categories.Category", on_delete=models.CASCADE)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    userip = models.TextField(max_length=16)
    