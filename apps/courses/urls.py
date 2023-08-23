from django.urls import path
from apps.courses.views import CoursesView, BenefitsView, MainMenuView, AboutView


urlpatterns = [
    path('', MainMenuView.as_view(), name='main-menu'),
    path('courses', CoursesView.as_view(), name='courses'),
    path('benefits', BenefitsView.as_view(), name='benefits'),
    path('about', AboutView.as_view(), name='about'),
]