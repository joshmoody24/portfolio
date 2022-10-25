from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(Skill)
admin.site.register(SkillCategory)
admin.site.register(Achievement)
admin.site.register(AchievementCategory)