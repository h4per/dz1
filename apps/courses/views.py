from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from apps.courses.models import Courses
from django.views import generic
from django.urls import reverse_lazy


class MainMenuView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = "courses/menu.html"
    context_object_name = "courses"


class CoursesView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = "courses/course.html"
    context_object_name = "courses"


class BenefitsView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = "courses/benefits.html"
    context_object_name = "courses"