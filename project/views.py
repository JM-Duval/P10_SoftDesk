from rest_framework import viewsets
from project.serializers import ProjectSerializer
from project.permissions import IsProjectAuthor, IsProjectContributor
from django.contrib.auth.models import User
from project.models import Project


class ProjectViewset(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsProjectAuthor | IsProjectContributor]
    
    def create(self, request, *args, **kwargs):
        request.POST._mutable = True  
        request.data["author_user_id"] = request.user.id
        request.POST_mutable = False 
        return super(ProjectViewset, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):  # peut être pas obligatoire
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.id
        request.POST_mutable = False
        return super(ProjectViewset, self).update(request, *args, **kwargs)

    def get_queryset(self):
        return Project.objects.filter(author_user_id=self.request.user)
        