from django.contrib import admin
from .models import Blog, Hit, Recom

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
    "title",
    "content",
    "author",
    "cate_no",
    "hits",
    "recoms",
    "created_at",
    "updated_at",
    )
    

@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "author",
        "userip",
    )    

@admin.register(Recom)
class RecomAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "author",
        "userip",
    )    