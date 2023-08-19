from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from apps.courses.models import Courses
from django.views import generic
from django.urls import reverse_lazy


class CoursesView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = "courses/index.html"
    context_object_name = "courses"

