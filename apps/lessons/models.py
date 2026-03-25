from django.db import models
from django.conf import settings

class Lesson(models.Model):
    module = models.ForeignKey('courses.Module', on_delete=models.RESTRICT, related_name='lessons')
    video = models.ForeignKey('media.Media', on_delete=models.RESTRICT, null=True, blank=True, related_name='video_lessons')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    current_rating = models.FloatField(default=0.0)
    lesson_type = models.CharField(max_length=100)
    max_attempts_count = models.IntegerField(default=3)
    attempt_interval = models.IntegerField(default=0)
    lesson_order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

class LessonQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT, related_name='questions')
    question_text = models.TextField()

class LessonAnswer(models.Model):
    question = models.ForeignKey(LessonQuestion, on_delete=models.RESTRICT, related_name='answers')
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)

class LessonResource(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT, related_name='resources')
    resource = models.ForeignKey('media.Media', on_delete=models.RESTRICT)

class LessonRate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT, related_name='ratings')
    rating = models.IntegerField()

class UserHomeworkAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT)
    score = models.IntegerField()


