from django.db import models
from django.contrib.auth.models import User


class RoleType(models.IntegerChoices):
    MEMBER = 0
    OWNER = 1


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("Category", on_delete=models.CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, through="Membership")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Membership(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    role = models.IntegerField(choices=RoleType)
