from rest_framework import serializers
from .models import Blog
from users.serializers import TinyUserSerializer
from categories.serializers import TinyCategorySerializer

class BlogSerializer(serializers.ModelSerializer):
    author = TinyUserSerializer(read_only=True)
    cate_no = TinyCategorySerializer(read_only=True)

    # postCount = serializers.SerializerMethodField()

    # def get_postCount(self):
    #     pCount = Blog.objects.all().count
    #     print(pCount)
    #     return "pCount"

    class Meta:
        model = Blog
        fields = ("title", "content","author","cate_no","updated_at","pk")

class CateBlogSerializer(serializers.ModelSerializer):
    author = TinyUserSerializer(read_only=True)
    cate_no = TinyCategorySerializer(read_only=True)

    # postCount = serializers.SerializerMethodField()

    # def get_postCount(self):
    #     pCount = Blog.objects.all().count
    #     print(pCount)
    #     return "pCount"

    class Meta:
        model = Blog
        fields = ("title", "content","author","cate_no","updated_at","pk")

        

class BlogDetailSerializer(serializers.ModelSerializer):
    author = TinyUserSerializer(read_only=True)
    cate_no = TinyCategorySerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ("title", "content","author","cate_no","updated_at","pk")

class BlogPostSerializer(serializers.ModelSerializer):
    author = TinyUserSerializer(read_only=True)
    # cate_no = TinyCategorySerializer(read_only=True)
    class Meta:
        model = Blog
        # fields = "__all__"
        fields = ("title", "content","author","cate_no")