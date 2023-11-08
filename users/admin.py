from django.contrib import admin

from users.models import Profile


@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user", 'image']