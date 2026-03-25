from django.db import models
from django.conf import settings

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    course = models.ForeignKey('courses.Course', on_delete=models.RESTRICT)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


