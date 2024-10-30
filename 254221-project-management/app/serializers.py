from rest_framework import serializers
from app.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "category",
            "members",
            "created_at",
            "updated_at",
        ]
