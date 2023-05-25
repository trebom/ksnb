from django.db import models
from common.models import CommonModel

class Category(CommonModel):
    name = models.CharField(max_length=150)
    upper_no = models.IntegerField()
    creator = models.ForeignKey("users.User", on_delete= models.CASCADE)
    depth = models.IntegerField()
    sub = models.IntegerField()

    def __str__(self):
        return str(self.pk)+"/"+ self.name+"/ "+str(self.upper_no)+"/ "+str(self.depth)
        
    class Meta:
        verbose_name_plural = "Categories"