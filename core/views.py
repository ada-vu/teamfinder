from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Skill, Profile, Project, Application

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'core/signup.html')

def profile(request):
    return render(request, 'core/user_profile.html')

class ProjectListView(generic.ListView):
    model = Project

class ApplicationListView(generic.ListView):
    model = Application

class ProjectApplicationsListView(generic.ListView):
    model = Application


class ProjectDetailView(generic.DetailView):
    model = Project

class ApplicationDetailView(generic.DetailView):
    model = Application


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project

class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application