from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import NotFound, NotAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.paginator import Paginator
from .models import Blog
from .serializers import BlogSerializer, CateBlogSerializer, BlogDetailSerializer, BlogPostSerializer
import json
PAGE_SIZE = 20
# -----------------------------------------------------------------

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication

class MyPagination(PageNumberPagination):
    page_size = PAGE_SIZE

class Blogs(ListAPIView):
    queryset = Blog.objects.all()
    # serialzer_class = BlogSerializer
    pagination_class = MyPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_class(self):
        return BlogSerializer

    def get(self, request ):  
        return self.list(request)

class BlogPostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request):
        if request.user.is_authenticated:
            serializer = BlogPostSerializer(data=request.data)
            if serializer.is_valid():
                blog = serializer.save(author=request.user)
                serializer = BlogPostSerializer(blog)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


# -----------------------------------------------------------------

# class Blogs(APIView):
    
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, request):
#         try:
#             page = request.query_params.get("page",1)
#             page = int(page)
#         except ValueError:
#             page = 1

#         page_size = PAGE_SIZE
#         start = (page-1) * page_size 
#         end = start + page_size
#         paginator = Paginator(Blog.objects.all(), page_size, orphans=2)
#         serializer = BlogSerializer(paginator.get_page(page), many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         if request.user.is_authenticated:
#             serializer = BlogPostSerializer(data=request.data)
#             if serializer.is_valid():
#                 blog = serializer.save(author=request.user)
#                 serializer = BlogPostSerializer(blog)
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
#         else:
#             raise NotAuthenticated
# -----------------------------------------------------------------

class CateBlogs(ListAPIView ):
    queryset = Blog.objects.all()
    # serialzer_class = BlogSerializer
    pagination_class = MyPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(cate_no=self.kwargs['pk'])

    def get_serializer_class(self):
        return CateBlogSerializer

    def get(self, request, pk ):  
        return self.list(request, pk)


# class CateBlogs(APIView):
#     def get(self, request, pk):
#         try:
#             page = request.query_params.get("page",1)
#             page = int(page)
#         except ValueError:
#             page = 1
#         page_size = 3
#         start = (page-1) * page_size 
#         end = start + page_size

#         serializer = BlogSerializer(Blog.objects.filter(cate_no=pk)[start:end], many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         if request.user.is_authenticated:
#             serializer = BlogPostSerializer(data=request.data)
#             if serializer.is_valid():
#                 blog = serializer.save(author=request.user)
#                 serializer = BlogPostSerializer(blog)
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
#         else:
#             raise NotAuthenticated

class BlogDetail(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise NotFound

    def put(self, request, pk):
        blog = self.get_object(pk)
        # body_unicode = request.body.decode('utf-8')
        # body_data = json.loads(body_unicode)
        # content = body_data.get('content')
        
        # Deserialize the request data using the BlogSerializer
        serializer = BlogSerializer(blog, data=request.data)
        serializer.is_valid(raise_exception=True)

        # Update the blog instance with the validated data
        serializer.save()

        # Return the updated blog data as JSON response
        return Response(serializer.data)

    def get(self, request, pk):
        try:
            blog = self.get_object(pk)
            serializer = BlogDetailSerializer(blog)
            return Response(serializer.data)
        except NotFound:
            return Response({"error":"404"}, status=404)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if blog.author != request.user:
            raise PermissionDenied
        blog.delete()
        return Response(status=HTTP_204_NO_CONTENT)