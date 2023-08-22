from django.contrib import admin
from apps.courses.models import Courses, Benefits

@admin.register(Courses)
class CoureseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status']
    list_filter = ["status"]
    list_editable = ["status"]


@admin.register(Benefits)
class Benefits(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status']
    list_filter = ["status"]
    list_editable = ["status"]