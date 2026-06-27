from django.shortcuts import render

from bio.models import Bio
from education.models import Education
from experience.models import Experience
from projects.models import Project
from skills.models import Skill


def index(request):
    """Single portfolio page — loads all content from the five apps."""
    context = {
        'bio': Bio.objects.first(),
        'education': Education.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'index.html', context)
