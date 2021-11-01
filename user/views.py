from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from user.models import User
from user.serializers import UserSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



@permission_classes([AllowAny,])
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully. Now perform Login to get your token",
            }
        )

"""
class UserViewset(ModelViewSet):

	serializer_class = UserSerializer

	def get_queryset(self):
		return User.objects.all()




@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    print('//////', user)
    try:
        email = request.data['email']
        password = request.data['password']
 
        user = User.objects.get(email=email, password=password)
        
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
 
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)




@permission_classes([AllowAny,])
class CreateUserAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny) # permet à tous les utilisateurs d'accéder à cette URL.
    print(':::::::::STEP 0')
    def post(self, request):
        user = request.data
        print(':::::::::STEP 1')
        #serializer = UserSerializer(data=user)
        print(user)
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        print(':::::::::STEP 2')
        
        serializer.save()
        print(':::::::::STEP 3')
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "user": serializer.data, 
                "message": "User Created Successfully. Now perform Login to get your token",
            }
        )




class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = UserSerializer(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

"""