from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer, CommentPostSerializer, CommentUpdateSerializer

# Create your views here.

class Comments(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound
        
    def get(self, request, blogid):
        comments = Comment.objects.filter(blogid=int(blogid)).order_by('-updated_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            
            serializer = CommentPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['author'] = request.user

                comment = serializer.save()
                response_serializer = CommentPostSerializer(comment)
                return Response(response_serializer.data)
            else:
                print(serializer.errors)
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


    def delete(self, request, commentid):
        comment = self.get_object(commentid) # 삭제할 자료
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if comment.author != request.user:
            raise PermissionDenied
        comment.delete()

        return Response(status=HTTP_204_NO_CONTENT)
