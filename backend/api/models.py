from django.db import models

# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    __str__ = lambda self: self.name
    class Meta:
        verbose_name_plural = "Project categories"

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
    class Meta:
        verbose_name_plural = "Skill categories"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.RESTRICT)
    order = models.IntegerField()
    featured = models.BooleanField()
    __str__ = lambda self: self.name

class AchievementCategory(models.Model):
    name = models.CharField(max_length=100)
    __str__ = lambda self: self.name
    class Meta:
        verbose_name_plural = "Achievement categories"

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

class University(models.Model):
    name = models.CharField(max_length=100)
    __str__ = lambda self: self.name
    class Meta:
        verbose_name_plural = "Universities"

class College(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    __str__ = lambda self: self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=5)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    __str__ = lambda self: self.name

class EducationStat(models.Model):
    education = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True)
    __str__ = lambda self: self.name

class DegreeType(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=5, blank=True)
    __str__ = lambda self: self.name

class Degree(models.Model):
    name = models.CharField(max_length=50)
    emphasis = models.CharField(max_length=50, blank=True)
    type = models.ForeignKey(DegreeType, on_delete=models.RESTRICT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    __str__ = lambda self: f'{self.type.name} {self.name}'

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    number = models.IntegerField(null=True)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    __str__ = lambda self: f'{self.department.abbreviation} {self.number}'

class Certification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    __str__ = lambda self: self.name

class Employment(models.Model):
    job_title = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50)
    __str__ = lambda self: f'{self.job_title} at {self.employer}'

class EmploymentDetail(models.Model):
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    description = models.TextField()
    __str__ = lambda self: self.description