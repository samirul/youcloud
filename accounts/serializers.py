from rest_framework import serializers

from accounts.models import User

from rest_framework.authtoken.models import Token


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]


    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )

        print(user)

        return user
    
# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Token
#         fields = [ 'created', 'key', 'user', 'user_id']


        # def validate(self, attrs):
        #     get_user = attrs('user')
        #     print(get_user.username)

        #     return attrs


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]