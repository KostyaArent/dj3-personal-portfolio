from django.contrib import admin
from .models import Project, Developer, ProgLanguage, Fact


admin.site.register(Project)
admin.site.register(Developer)
admin.site.register(ProgLanguage)
admin.site.register(Fact)
