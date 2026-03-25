from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Education, UserEducation, UserExperience, UserCertificate, Author

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'phone', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'gender')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_education', 'is_active')
    search_fields = ('name', 'type_education')
    list_filter = ('is_active', 'type_education')

@admin.register(UserEducation)
class UserEducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'education', 'field', 'start_date', 'end_date')
    search_fields = ('user__username', 'field', 'education__name')

@admin.register(UserExperience)
class UserExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'position', 'start_date', 'end_date')
    search_fields = ('user__username', 'name', 'position')

@admin.register(UserCertificate)
class UserCertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'name')
    search_fields = ('user__username', 'name', 'course__name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'experience_years')
    search_fields = ('first_name', 'last_name')

