# import re
# from rest_framework import serializers
# from accounts.models import User



# class GetUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "email"]


# class RegisterModelSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#     class Meta:
#         model = User
#         fields = ["username", "email", "password", "confirm_password"]

#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#     def validate(self, attrs):
#         password = attrs.get("password")
#         confirm_password = attrs.get("confirm_password")
#         if password != confirm_password:
#             raise serializers.ValidationError("Password and Confirm password doesn't match.")
        
#         if len(password) < 8:
#             raise serializers.ValidationError("Password should be minimum 8 digits.")
        
#         if not re.search(r'[A-Z]', password):
#             raise serializers.ValidationError("Password should have atleast one uppercase.")

#         if not re.search(r'[a-z]', password):
#             raise serializers.ValidationError("Password should have atleast one lowercase.")
        
#         if not re.search(r'[0-9]', password):
#             raise serializers.ValidationError("Password should have atleast one number.")
        
#         if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', password):
#             raise serializers.ValidationError("Password should have atleast one special character.")
        
#         return attrs
    
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)

# class LoginModelSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=255)
#     class Meta:
#         model = User
#         fields = ['email', 'password']




























# # class UserModelSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = ["id", "username", "email", "password"]
# #         extra_kwargs = {
# #             'password': {'write_only': True}
# #         }


# #     def create(self, validated_data):
# #         user = User.objects.create_user(
# #             username = validated_data['username'],
# #             email = validated_data['email'],
# #             password = validated_data['password']
# #         )

# #         return user