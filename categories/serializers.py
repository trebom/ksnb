from rest_framework import serializers
from .models import Category
from blogs.models import Blog
from users.serializers import TinyUserSerializer

class CategorySerializer(serializers.ModelSerializer):

    creator = TinyUserSerializer(read_only=True)

    postCount = serializers.SerializerMethodField()

    def get_postCount(self, catePk):
       pCount = Blog.objects.filter(cate_no=catePk).count()
       return pCount

    class Meta:
        model = Category
        fields = ("name", "creator","upper_no","pk", "postCount", "depth","sub")

class CategoryDetailSerializer(serializers.ModelSerializer):
    
    creator = TinyUserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class CategoryPostSerializer(serializers.ModelSerializer):
    
    creator = TinyUserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ("name","creator","upper_no", "depth", "sub")

class CategoryUpdateSerializer(serializers.ModelSerializer):
    
    creator = TinyUserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ("name","creator")

class TinyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "upper_no",
            "pk",
        )
    