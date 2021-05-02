from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Skill, Profile, Project, Application

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    return render(request, 'core/signup.html')

def profile(request):
    return render(request, 'core/user_profile.html')

class ProjectListView(generic.ListView):
    model = Project

class ApplicationListView(generic.ListView):
    model = Application

class ProjectApplicationsListView(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = "core/project_application_list.html"

    def get_queryset(self):
        project_applications = {}
        projects_queries = Project.objects.filter(creator__user=self.request.user)
        for project in projects_queries:
            applications = []
            applications_queries = Application.objects.filter(project__title=project.title,
                                                              project__creator=project.creator)
            for application in applications_queries:
                applications.append(application)
            project_applications[project.title] = applications

        return "Application.objects.filter"


class ProjectDetailView(generic.DetailView):
    model = Project

class ApplicationDetailView(generic.DetailView):
    model = Application


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project

class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
