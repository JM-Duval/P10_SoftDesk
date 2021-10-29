from rest_framework.permissions import BasePermission
from rest_framework import permissions
from contributor.models import Contributor


class IsProjectAuthor(BasePermission):

    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_object_permission(self, request, view, obj):
               
        if obj.author_user_id.id == request.user.id:
            return True


class IsProjectContributor(BasePermission):

    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_object_permission(self, request, view, obj):
        index_project = obj.id
        contributors_in_project = Contributor.objects.filter(project_id__id=index_project)
        for contributor in contributors_in_project:
            if contributor.user_id.id == request.user.id:
                return True
        