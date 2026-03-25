from django.contrib import admin
from .models import Lesson, LessonQuestion, LessonAnswer, LessonResource, LessonRate, UserHomeworkAttempt

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'lesson_type', 'lesson_order', 'is_active')
    search_fields = ('name', 'module__name', 'lesson_type')
    list_filter = ('is_active', 'lesson_type', 'module')

@admin.register(LessonQuestion)
class LessonQuestionAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'question_text')
    search_fields = ('question_text', 'lesson__name')

@admin.register(LessonAnswer)
class LessonAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_correct')
    search_fields = ('answer_text', 'question__question_text')
    list_filter = ('is_correct',)

@admin.register(LessonResource)
class LessonResourceAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'resource')

@admin.register(LessonRate)
class LessonRateAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'rating')
    list_filter = ('rating',)

@admin.register(UserHomeworkAttempt)
class UserHomeworkAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'score')
    search_fields = ('user__username', 'lesson__name')

