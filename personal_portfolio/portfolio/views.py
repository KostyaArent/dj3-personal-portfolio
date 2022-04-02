from django.shortcuts import render
from .models import Project, Developer, Fact
import random

def home(request):
    projects = Project.objects.all()
    developer = Developer.objects.first()
    languages = list(developer.languages.values_list('title', flat=True))
    languages_str = ', '.join([language for language in languages])
    facts = list(developer.facts.values_list('description', flat=True))
    fact = facts[random.randint(0, len(facts)-1)]
    return render(request, 'portfolio/home.html',{'projects':projects, 'languages_str': languages_str, 'fact':fact})
