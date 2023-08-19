from django.contrib import admin
from apps.courses.models import Courses

@admin.register(Courses)
class CoureseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status']
    list_filter = ["status"]
    list_editable = ["status"]