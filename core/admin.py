from django.contrib import admin
from .models import Skill, Profile, Project, Application

# Register your models here.
admin.site.register(Application)
admin.site.register(Skill)

class ProjectInline(admin.TabularInline):
    model = Project

class ApplicationInline(admin.TabularInline):
    model = Application

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [ProjectInline, ApplicationInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ApplicationInline]