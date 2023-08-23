from django.contrib import admin
from apps.courses.models import Courses, Benefits, About, Faq, Enroll

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


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'status', 'answer']
    list_filter = ['status']


@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display =  ["name", "surname", "course", "email", "phone_number"]
    list_filter = ['status']
