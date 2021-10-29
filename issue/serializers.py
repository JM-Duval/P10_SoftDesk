from rest_framework.serializers import ModelSerializer

from issue.models import Issue

class IssueSerializer(ModelSerializer):

	class Meta:
		model = Issue
		fields = ['id', 'title', 'description', 'tag', 'priority', 'project_id', 'status', 
				  'assignee_user_id', 'created_time']
		


