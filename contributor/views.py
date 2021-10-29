from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import viewsets
from contributor.models import Contributor
from contributor.serializers import ContributorSerializer
from project.models import Project
from user.models import User
from rest_framework.exceptions import ValidationError


class ContributorViewset(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    
    def create(self, request, *args, **kwargs):            
        index_project = int(kwargs["projects_pk"])
        index_user = int(request.data['user_id'])
        contributors_in_project = Contributor.objects.filter(project_id__id=index_project)
        if contributors_in_project.filter(user_id__id=index_user).exists():
            raise ValidationError("contributor existe déjà dans la liste")
        else:
            request.POST._mutable = True
            print(kwargs["projects_pk"])
            request.data["project_id"] = kwargs["projects_pk"]
            request.POST_mutable = False
            return super(ContributorViewset, self).create(request, *args, **kwargs)


    def list(self, request, *args, **kwargs):
        index_project = int(kwargs["projects_pk"])
        contributors = Contributor.objects.filter(project_id__id=index_project)
        serializer = ContributorSerializer(contributors, many=True)
        return Response(serializer.data)
   

    def get_queryset(self):
        return Contributor.objects.all()





    """
    def create(self, request, *args, **kwargs):

        request.POST._mutable = True
        index_project = int(kwargs["projects_pk"])
        project = Project.objects.get(id=index_project)
        print(project.contributor)
        print(type(project))
        
        #print(Project.objects.filter(id=index_project))


        print(request.data['user_id'])
        print(kwargs)

        request.data["project_id"] = kwargs["projects_pk"]
        print(' //////// ', request.data["project_id"])
        request.POST._mutable = False
        return super(ContributorViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        request.POST._mutable = True
        print('//// Test //// ')
        projects = Project.objects.all()
        #index = int(request.data['project_id'])
        for project in projects:
            print(project.title, project.id, type(project.contributor))
        print(' ******* resquest.id ******* ', request)
        print(kwargs['pk'])
        print(request.data.get('address_pk'))
        request.POST_mutable = False
        return super(ContributorViewset, self).destroy(request, *args, **kwargs)
    """