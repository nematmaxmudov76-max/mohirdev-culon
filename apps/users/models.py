from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Standard AbstractUser already provides first_name, last_name, password, last_login, is_staff, is_superuser, is_active
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    avatar = models.ForeignKey('media.Media', on_delete=models.RESTRICT, null=True, blank=True, related_name='user_avatars')
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    country_id = models.IntegerField(null=True, blank=True) # Assuming no Country model in schema
    region_id = models.IntegerField(null=True, blank=True) # Assuming no Region model in schema
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Education(models.Model):
    name = models.CharField(max_length=255)
    type_education = models.CharField(max_length=100)
    website_url = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

class UserEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='educations')
    education = models.ForeignKey(Education, on_delete=models.RESTRICT)
    field = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class UserExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='experiences')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    website_url = models.URLField(null=True, blank=True)
    skills = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class UserCertificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='certificates')
    course = models.ForeignKey('courses.Course', on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)
    attachment = models.ForeignKey('media.Media', on_delete=models.RESTRICT, null=True, blank=True)

class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    description = models.TextField()
    avatar = models.ForeignKey('media.Media', on_delete=models.RESTRICT, null=True, blank=True)
    experience_years = models.IntegerField(default=0)

