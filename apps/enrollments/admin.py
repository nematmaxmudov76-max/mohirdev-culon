from django.contrib import admin
from .models import Enrollment, Notification

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    search_fields = ('user__username', 'course__name')
    list_filter = ('enrolled_at',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    search_fields = ('user__username', 'message')
    list_filter = ('is_read', 'created_at')

