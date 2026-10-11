from django.contrib import admin

from .models import Announcement, Registration


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_editable = ("is_active",)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "school_class", "phone", "created_at")
    list_filter = ("school_class",)
    search_fields = ("last_name", "first_name", "phone")
