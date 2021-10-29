from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from project.models import Project
from project.serializers import ProjectSerializer
from project.permissions import IsProjectAuthor, IsProjectContributor
from contributor.views import ContributorViewset
from contributor.serializers import ContributorSerializer
from rest_framework.permissions import IsAuthenticated


class ProjectViewset(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
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

    #@permission_required('IsProjectAuthor', raise_exception=True)
    def get_queryset(self):
        #return Project.objects.filter(author_user_id=self.request.user)
        return Project.objects.all()













    """
    @action(detail=True, methods=['get'])
    def users(self, request, *args, **kwargs):
        project = self.get_object()
        #target_project = int(kwargs['target_id'])

        print(project.title)
        print(project.description)
        print(type(project))
        print(args)
        print(kwargs)

        print('///// REQUEST /////////', request)
        print('///// REQUEST /////////', type(request))
        print('//////// PROJECT ////////',project.contributor)
        
        queryset = Project.objects.all()

        #serializer_class = ContributorSerializer
        #test = Contributor.objects.all()
        #return Response(ContributorSerializer)
        return Response(queryset)
    
       
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
     


    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    """



    """
class ProjectAPIView(GenericAPIView):
    
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, *arg, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)




 
    def get(self, request, format=None):
        projects = Project.objects.all()
        print(projects)
        serializer = ProjectSerializer(projects, many=True)
        print(serializer.data)
        return Response(serializer.data)


    def get(self, request, format=None):
        
        #Return a list of all users.
        
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
    """


    """
    
    def get(self, *args, **kwargs):
        
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
        #return Project.objects.all()
    

    def project(request):
        project_form = ProjectForm(request.POST)
        if request.method == 'POST':
            print('////////', request.user.id)
            new_project = project_form.save(commit=False)
            new_project.author_user_id = request.user.id
            new_project.save()


    """


