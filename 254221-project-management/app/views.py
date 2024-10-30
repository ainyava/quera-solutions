from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from app.serializers import ProjectSerializer
from app.models import Project


class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()
