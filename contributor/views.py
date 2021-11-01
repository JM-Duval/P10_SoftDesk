from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import viewsets
from contributor.models import Contributor
from contributor.serializers import ContributorSerializer
from project.models import Project
from user.models import User
from rest_framework.exceptions import ValidationError
from contributor.permissions import IsProjectAuthor, IsProjectContributor


class ContributorViewset(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsProjectAuthor | IsProjectContributor]

    def create(self, request, *args, **kwargs):            
        index_project = int(kwargs["projects_pk"])
        index_user = int(request.data['user_id'])
        contributors_in_project = Contributor.objects.filter(
            project_id__id=index_project)
        if contributors_in_project.filter(user_id__id=index_user).exists():
            raise ValidationError("contributor existe déjà dans la liste")
        else:
            request.POST._mutable = True
            print(kwargs["projects_pk"])
            request.data["project_id"] = kwargs["projects_pk"]
            request.POST_mutable = False
            return super(ContributorViewset, self).create(
                request, *args, **kwargs)


    def list(self, request, *args, **kwargs):
        index_project = int(kwargs["projects_pk"])
        contributors = Contributor.objects.filter(project_id__id=index_project)
        serializer = ContributorSerializer(contributors, many=True)
        return Response(serializer.data)
   

    def get_queryset(self):
        return Contributor.objects.all()
