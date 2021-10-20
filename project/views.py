from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from project.models import Project
from project.serializers import ProjectSerializer

# class AdminProjectViewset()

class ProjectViewset(ModelViewSet):

	serializer_class = ProjectSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Project.objects.all()


"""
class ProjectAPIView(APIView):

	def get(self, *args, **kwargs):
		
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, many=True)
		return Response(serializer.data)

def project(request):
	project_form = ProjectForm(request.POST)
	if request.method == 'POST':
		new_project = project_form.save(commit=False)
		new_project.author_user_id = request.user.id
		new_project.save()



	#project_id = models.IntegerField(default=0)
	title = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	#type = models.CharField(max_length=128)
	author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, 
    	on_delete=models.CASCADE)

"""

