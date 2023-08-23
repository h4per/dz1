from apps.courses.models import Courses, Benefits, About
from django.views import generic



class MainMenuView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = "courses/menu.html"
    context_object_name = "courses"


class CoursesView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = "courses/courses.html"
    context_object_name = "courses"


class BenefitsView(generic.ListView):
    queryset = Benefits.objects.all()
    template_name = "courses/benefits.html"
    context_object_name = "benefits"

class AboutView(generic.ListView):
    queryset = About.objects.all()
    template_name = "courses/about.html"
    context_object_name = "abouts"