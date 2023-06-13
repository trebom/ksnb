from django.urls import path
from . import views

urlpatterns = [
   path("", views.Comments.as_view()),
   path("<int:blogid>/", views.Comments.as_view()),
   path("post/", views.Comments.as_view()),
   path("delete/<int:commentid>/", views.Comments.as_view()),
   
]