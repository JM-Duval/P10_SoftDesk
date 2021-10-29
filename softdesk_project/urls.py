from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#from project.views import ProjectAPIView
from project.views import ProjectViewset #, AdminProjectViewset
from user.views import UserViewset, RegisterApi
from issue.views import IssueViewset
from comment.views import CommentViewset
from contributor.views import ContributorViewset


# création du routeur
router = routers.SimpleRouter()
# déclaration de project afin de générer l'URL correspondante

projects_router = routers.SimpleRouter(trailing_slash=False)
projects_router.register(r"projects/?", ProjectViewset)

users_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
users_router.register(r"users/?", ContributorViewset, basename="users")

issues_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
issues_router.register(r"issues/?", IssueViewset, basename="issues")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues", trailing_slash=False)
comments_router.register(r"comments/?", CommentViewset, basename="comments")



router.register('projects/?', ProjectViewset, basename='projects')
#router.register('projects/users', ContributorViewset, basename='contributor')
router.register('users', UserViewset, basename='user')
router.register('comment', CommentViewset, basename='comment')	
router.register('issue', IssueViewset, basename='issue')
router.register('contributor', ContributorViewset, basename='contributor')

#router.register('admin/project', AdminProjectViewset, basename='admin-project')


urlpatterns = [
	path("", include(projects_router.urls)),
	path("", include(users_router.urls)),
	path("", include(issues_router.urls)),
	path("", include(comments_router.urls)),
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),    
	path('signup/', RegisterApi.as_view(), name='signup'),
	path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
	path('', include(router.urls)), # urls du router pour rendre les urls disponibles
	#path('', include('user.urls')),
]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
