from django.urls import path
from . import views

urlpatterns = [
   path("", views.Blogs.as_view()),
   path("<int:pk>", views.BlogDetail.as_view()),
   path("post/", views.BlogPostView.as_view()),
   path("update/<int:pk>", views.BlogDetail.as_view()),
   path("delete/<int:pk>", views.BlogDetail.as_view()),
   path("cate/<int:pk>", views.CateBlogs.as_view()),
]