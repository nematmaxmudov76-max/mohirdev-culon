from celery import shared_task
from django.db.models import Avg

from apps.courses.models import Lesson
from apps.interactions.models import LessonRate

@shared_task
def calculate_lesson_ratings():

    lessons = LessonRate.objects.filter(is_active = True)
    update_count = 0

    for lesson in lessons:
        avg = LessonRate.objects.filter(lesson = lesson).aggregate(avg_rating = Avg("star_count"))["avg_rating"]

        new_ratting = round(avg, 2) if avg else 0.0

        if Lesson.current_rating != new_ratting:
            lesson.current_rating = new_ratting
            lesson.save(update_fields=["current_rating"])
            update_count += 1
    return f"updated ratings for{update_count} lesson"

        