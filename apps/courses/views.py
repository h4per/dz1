from apps.courses.models import Courses, Benefits, About, Faq, Enroll
from django.views import generic
from django.urls import reverse_lazy
from apps.courses.forms import EnrollForm


class MainMenuView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = "courses/menu.html"
    context_object_name = "courses"


class CoursesView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = "courses/courses.html"
    context_object_name = "courses"


class CourseDetailView(generic.DetailView):
    model = Courses
    template_name = "courses/courses_detail.html"
    context_object_name = "courses"    


class EnrollCreateView(generic.CreateView):
    model = Enroll
    template_name = "courses/enroll.html"
    form_class = EnrollForm
    success_url = reverse_lazy("courses")


class BenefitsView(generic.ListView):
    queryset = Benefits.objects.all()
    template_name = "courses/benefits.html"
    context_object_name = "benefits"


class AboutView(generic.ListView):
    queryset = About.objects.all()
    template_name = "courses/about.html"
    context_object_name = "abouts"


class FaqView(generic.ListView):
    queryset = Faq.objects.all()
    template_name = "courses/faq.html"
    context_object_name = "faqs"
