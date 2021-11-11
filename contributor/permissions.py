from rest_framework.permissions import BasePermission
from rest_framework import permissions
from issue.models import Issue
from project.models import Project
from contributor.models import Contributor


METHODES_CREATE_READ = [ 'GET', 'POST' ]
METHODES_PUT_DEL = [ 'PUT', 'DELETE']


class IsProjectAuthor(BasePermission):
    """Author of project can Create and Read issues"""
    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_permission(self, request, view):
        index_project = view.kwargs['projects_pk']
        project = Project.objects.get(id=index_project)
        if project.author_user_id.id == request.user.id: # si le user est l'autheur du projet
            print("l'utilisateur est l'auteur du projet")
            print(request.method)
            if (request.method in METHODES_CREATE_READ or 
                request.method in METHODES_PUT_DEL):  # Pour lecture et ecriture
                return True


class IsProjectContributor(BasePermission):
    """Contributors of project can Create and Read issues"""
    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_permission(self, request, view):
        index_project = view.kwargs['projects_pk']
        contributeurs_project = Contributor.objects.filter(
            project_id__id=index_project)
        for contributor in contributeurs_project:
            if contributor.user_id.id == request.user.id: #
                if request.method in METHODES_CREATE_READ: # Pour lecture et ecriture
                    print("l'utilisateur est un des contributors du projet")
                    return True