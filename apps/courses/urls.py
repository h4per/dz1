from django.urls import path
from apps.courses.views import CoursesView, BenefitsView


urlpatterns = [
    path('', CoursesView.as_view(), name='courses'),
    path('benefits/', BenefitsView.as_view(), name='benefits'),
]