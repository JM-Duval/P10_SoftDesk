from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import viewsets
from comment.serializers import CommentSerializer
from comment.permissions import IsProjectAuthor, IsProjectContributor, IsCommentAuthor
from issue.models import Issue
from comment.models import Comment


class CommentViewset(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [ 
        IsProjectAuthor | IsProjectContributor | IsCommentAuthor 
        ]

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.id
        request.data["issue_id"] = int(kwargs["issues_pk"])
        request.POST_mutable = False
        return super(CommentViewset, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        index_issue = kwargs['issues_pk']
        queryset = Issue.objects.filter(id=index_issue)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.all()
