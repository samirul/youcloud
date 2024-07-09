import uuid
import requests
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.core.files.base import ContentFile

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, username, email, password):

        user = self.create_user(
            username=username,
            email=email,
            password=password,
            
        )
        
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
    



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique = True)
    profilePic = models.ImageField(upload_to='profile-pic', default="default.png")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_all_permissions(self, user=None):
        if user.is_admin:
            return set()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

@receiver(user_logged_in, sender=User) 
def save_google_profile_image(sender, request, user, **kwargs):
    social_account = user.socialaccount_set.filter(provider='google').first()
    pic = User.objects.get(email=user)
    if social_account:
        extra_data = social_account.extra_data
        profile_image_url = extra_data.get('picture')
        
        if profile_image_url and pic.profilePic =='default.png':
            response = requests.get(profile_image_url, timeout=5)
            if response.status_code == 200:
                user.profilePic.save(
                    f"{user.username}__google_user_profile.jpg",
                    ContentFile(response.content)
                )
                user.save()
    


    
