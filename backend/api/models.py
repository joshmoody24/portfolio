from django.db import models

# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    __str__ = lambda self: self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.RESTRICT)
    order = models.IntegerField()
    featured = models.BooleanField()
    url = models.URLField()
    __str__ = lambda self: self.name

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    __str__ = lambda self: self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(SkillCategory, on_delete=models.RESTRICT)
    order = models.IntegerField()
    featured = models.BooleanField()
    __str__ = lambda self: self.name

class AchievementCategory(models.Model):
    name = models.CharField(max_length=100)
    __str__ = lambda self: self.name

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(AchievementCategory, on_delete=models.RESTRICT)
    order = models.IntegerField()
    featured = models.BooleanField()
    __str__ = lambda self: self.name

class Setting(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)