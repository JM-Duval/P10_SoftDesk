from rest_framework.viewsets import ModelViewSet

from issue.models import Issue
from issue.serializers import IssueSerializer


class IssueViewset(ModelViewSet):

	serializer_class = IssueSerializer

	def get_queryset(self):
		return Issue.objects.all()

