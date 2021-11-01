from rest_framework.permissions import BasePermission
from rest_framework import permissions
from project.models import Project
from contributor.models import Contributor
from issue.models import Issue


METHODES_CREATE_READ = [ 'GET', 'POST' ]
METHODES_PUT_DEL = [ 'PUT', 'DELETE']


class IsProjectAuthor(BasePermission):
    """Author of project can Create and Read comments"""
    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_permission(self, request, view):
        print(view.kwargs)
        index_project = view.kwargs['projects_pk']
        project = Project.objects.get(id=index_project)
        if project.author_user_id.id == request.user.id: # si le user est l'autheur du projet
            if request.method in METHODES_CREATE_READ: # Pour lecture et ecriture
                print('l utilisateur est l author du projet')
                return True


class IsProjectContributor(BasePermission):
    """Contributors of project can Create and Read comments"""
    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_permission(self, request, view):
        index_project = view.kwargs['projects_pk']
        contributeurs_project = Contributor.objects.filter(
            project_id__id=index_project)
        for contributor in contributeurs_project:
            if contributor.user_id.id == request.user.id: #
                print(request.method)
                if request.method in METHODES_CREATE_READ: # Pour lecture et ecriture
                    print('l utilisateur est un contributeur du projet')
                    return True


class IsCommentAuthor(BasePermission):
    """Author of Issue can Update and Delete issues """
    message = "L'utilisateur doit être l'auteur du commentaire"

    def has_permission(self, request, view):
        print(view.kwargs['pk'])
        id_issue = view.kwargs['issues_pk']
        issue = Issue.objects.get(id=id_issue)
        if issue.assignee_user_id.id == request.user.id: # si l'utilisateur est l'auteur du problème
            if request.method in METHODES_PUT_DEL: # pour MAJ et suppression
                return True