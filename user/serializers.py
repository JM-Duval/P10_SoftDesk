from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from user.models import User

""" 
class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        #extra_kwargs = {'password': {'write_only':True}}
        #extra_kwargs = {'password':}

        def validate_password(self, password: str):
            #Hash password passed by user.

            #:param password: password of a user
            #:return: a hashed version of the password

            if password is not None:
                return make_password(password)


"""

"""
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password")
        extra_kwargs = {"password": {"write_only": True},}


    def create(self, validated_data):
        return User.objects.create_user(
            validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )
   
"""

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        #fields = ("id", "username","first_name", "last_name", "password", "email")
        fields = ("first_name", "last_name", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            #validated_data["username"],
            #username=validated_data["first_name"],
            password=validated_data["password"],
            email=validated_data["email"],
        )


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")
