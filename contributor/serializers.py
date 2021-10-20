from rest_framework.serializers import ModelSerializer

from contributor.models import Contributor

class ContributorSerializer(ModelSerializer):

	class Meta:
		model = Contributor
		fields = ['user_id', 'project_id', 'permission', 'role']
