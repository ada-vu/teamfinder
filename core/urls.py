from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('projects/create', views.ProjectCreate.as_view(), name="create-projects"),
    path('projects/', views.ProjectListView.as_view(), name="projects"),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name="project-detail"),
    path('projects/<int:pk>/apply', views.create_application_view, name="create-applications"),
    path('projects/applications', views.ProjectApplicationsListView.as_view(), name="project-applications"),

    path('applications/', views.ApplicationListView.as_view(), name="applications"),
    path('applications/<int:pk>', views.ApplicationDetailView.as_view(), name="application-detail"),
    path('applications/decision/<int:pk>', views.update_application, name="application-decision"),
]
