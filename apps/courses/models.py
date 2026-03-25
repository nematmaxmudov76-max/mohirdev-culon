from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    author = models.ForeignKey('users.Author', on_delete=models.RESTRICT)
    banner = models.ForeignKey('media.Media', on_delete=models.RESTRICT, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    reward_stars = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

class CourseTag(models.Model):
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, related_name='modules')
    name = models.CharField(max_length=255)
    course_order = models.IntegerField(default=1)


