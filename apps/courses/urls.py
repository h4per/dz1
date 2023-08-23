from django.urls import path
from apps.courses.views import CoursesView, BenefitsView, MainMenuView, AboutView, FaqView, CourseDetailView, EnrollCreateView


urlpatterns = [
    path('', MainMenuView.as_view(), name='main-menu'),
    path('courses', CoursesView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='courses-detail'),
    path('enroll', EnrollCreateView.as_view(), name='enroll'),
    path('benefits', BenefitsView.as_view(), name='benefits'),
    path('about', AboutView.as_view(), name='about'),
    path('faq', FaqView.as_view(), name='faq'),
]