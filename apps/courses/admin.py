from django.contrib import admin
from apps.courses.models import Courses, Benefits, About

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status']
    list_filter = ['status']


@admin.register(Benefits)
class BenefitsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']
    list_filter = ['status']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['description', 'status', 'image']
    list_filter = ['status']