from rest_framework.serializers import ModelSerializer

from project.models import Project

class ProjectSerializer(ModelSerializer):


	class Meta:
		model = Project
		fields = ['id', 'title', 'description', 'type_project', 
			'author_user_id']