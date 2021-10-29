from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from issue.models import Issue
from issue.serializers import IssueSerializer
from issue.permissions import IsProjectAuthor, IsProjectContributor, IsIssueAuthor


class IssueViewset(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsProjectAuthor | IsProjectContributor | IsIssueAuthor]

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["assignee_user_id"] = request.user.id
        request.data["project_id"] = kwargs["projects_pk"]
        request.POST_mutable = False
        return super(IssueViewset, self).create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["assignee_user_id"] = request.user.id
        request.data["project_id"] = kwargs["projects_pk"]
        request.POST_mutable = False
        return super(IssueViewset, self).update(request, *args, **kwargs)

    def get_queryset(self):
        return Issue.objects.all()

