from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Skill(models.Model):
    skill = models.CharField(
        primary_key=True,
        max_length=100,
        help_text="Hard skills you possess")


class Profile(models.Model):
    FEMALE = "F"
    MALE = "M"
    TRANSGENDER = "T"
    OTHERS = "O"

    GENDER_CHOICES = [
        (FEMALE, "Female"),
        (MALE, "Male"),
        (TRANSGENDER, "Transgender"),
        (OTHERS, "Others"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, blank=True, default="Unspecified")
    description = models.TextField(max_length=2500, null=True, blank=True)
    skills = models.ManyToManyField(
        "Skill",
        blank=True,
        help_text="Choose technical skills you have")
    education = models.CharField(max_length=200, null=True, blank=True)
    resume = models.FileField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=GENDER_CHOICES)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user', 'role']

    def get_absolute_url(self):
        return reverse('user-profile', args=[str(self.id)])

    def __str__(self):
        return self.user.get_full_name()


class Project(models.Model):
    IDEATION = "ID"
    PLANNING = "PL"
    DESIGN = "DES"
    DEVELOPMENT = "DEV"
    DEPLOYED = "DEP"

    DEVELOPMENT_PHASE_CHOICES = [
        (IDEATION, "Ideation"),
        (PLANNING, "Planning"),
        (DESIGN, "Design"),
        (DEVELOPMENT, "Development"),
        (DEPLOYED, "Deployed"),
    ]

    creator = models.ForeignKey("Profile", related_name="+", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(
        "Profile",
        blank=True,
        related_name="+",
        help_text="Add your team members to this project")
    description = models.TextField(
        max_length=2500,
        help_text="Talk about how exciting your project is and what it entails!")
    preferred_role = models.CharField(max_length=100)
    preferred_skills = models.ManyToManyField(
        "Skill",
        blank=True,
        related_name="+",
        help_text="Choose skills you prefer in your potential teammate")
    team_skills = models.ManyToManyField(
        "Skill",
        blank=True,
        related_name="+",
        help_text="Choose skills your team has")
    development_phase = models.CharField(
        max_length=200,
        choices=DEVELOPMENT_PHASE_CHOICES,
        help_text="Choose your current development phase")
    expected_end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['created_date', 'title', 'creator']

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

    def __str__(self):
        return "Project: {0} created by {1}".format(self.title, self.creator)


class Application(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    cover_letter = models.TextField(
        max_length=1500,
        blank=True,
        default="I am interested in working on this project!")

    class Meta:
        ordering = ['profile', 'project']

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.id)])

    def __str__(self):
        return "{0} applied to {1}".format(self.profile, self.project)

