from django.urls import path
from apps.courses.views import CoursesView


urlpatterns = [
    path('', CoursesView.as_view(), name='courses')
]