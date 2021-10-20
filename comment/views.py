from rest_framework.viewsets import ModelViewSet

from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentViewset(ModelViewSet):

	serializer_class = CommentSerializer

	def get_queryset(self):
		return Comment.objects.all()