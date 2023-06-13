from rest_framework import serializers
from .models import Comment
from users.serializers import TinyUserSerializer


class CommentCountSerializer(serializers.ModelSerializer):
    
    commentCount = serializers.SerializerMethodField()

    def get_commentCount(self, obj):
        blogid = obj.blogid
        if isinstance(blogid, int):
            pCount = Comment.objects.filter(blogid=blogid).count()
        else:
            pCount = Comment.objects.filter(blogid=int(blogid)).count()
        return pCount
    class Meta:
        model = Comment
        fields = ("commentCount")


class CommentSerializer(serializers.ModelSerializer):

    author = TinyUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "author","imageUrl","comment", "blogid", "created_at", "updated_at")

class CommentDetailSerializer(serializers.ModelSerializer):
    
    author = TinyUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class CommentPostSerializer(serializers.ModelSerializer):
    
    author = TinyUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("author","imageUrl","comment", "blogid")

class CommentUpdateSerializer(serializers.ModelSerializer):
    
    author = TinyUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("comment","author")

class TinyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "author",
            "comment",
            "pk",
        )
    