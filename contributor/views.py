from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from contributor.models import Contributor
from contributor.serializers import ContributorSerializer



class ContributorViewset(ModelViewSet):

	serializer_class = ContributorSerializer

	def get_queryset(self):
		return Contributor.objects.all()