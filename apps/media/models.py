from django.db import models

class Media(models.Model):
    file_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

