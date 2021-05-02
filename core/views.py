<<<<<<< Updated upstream
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
=======
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
>>>>>>> Stashed changes
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Skill, Profile, Project, Application
from .forms import ApplicationForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "core/about.html")

<<<<<<< Updated upstream
def signup(request):
    return render(request, 'core/signup.html')
=======
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "core/signup.html"
>>>>>>> Stashed changes

def profile(request):
    return render(request, "core/user_profile.html")

class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 9

class ApplicationListView(generic.ListView):
    model = Application
    paginate_by = 12

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
    fields = ["title", "members", "description", "preferred_role",
              "preferred_skills", "team_skills", "development_phase", "expected_end_date"]
    success_url = reverse_lazy("projects")

    def form_valid(self, form):
        form.instance.creator = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


def create_application_view(request, pk):

    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():

            try:
                project = Project.objects.get(pk=pk)
            except Project.DoesNotExist:
                raise Http404('Project does not exist')

            application = form.save(commit=False)

            application.profile = Profile.objects.get(user=request.user)
            application.project = project
            
            form.save()

            return redirect('projects')
    else:
        profile = Profile.objects.get(user=request.user)

        form = ApplicationForm(initial={"profile": profile})

    return render(request, 'core/application_form.html', {'form': form, 'pk': pk})


def create_application(request, pk, **kwargs):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404('Project does not exist')
    
    return render(request, 'core/projects_list.html')