from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentViewset(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.id
        request.data["issue_id"] = int(kwargs["issues_pk"])
        request.POST_mutable = False
        return super(CommentViewset, self).create(request, *args, **kwargs)

    def get_queryset(self):
        return Comment.objects.all()
