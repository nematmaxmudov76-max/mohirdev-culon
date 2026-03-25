from django.contrib import admin
from .models import Category, Tag, Course, CourseTag, Module

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'reward_stars', 'is_active', 'is_published')
    search_fields = ('name', 'description', 'author__first_name', 'author__last_name')
    list_filter = ('is_active', 'is_published', 'category')

@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = ('course', 'tag')
    search_fields = ('course__name', 'tag__name')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'course_order')
    search_fields = ('name', 'course__name')
    list_filter = ('course',)

