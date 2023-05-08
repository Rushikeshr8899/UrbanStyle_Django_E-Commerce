from django.db import models as m
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self,email,username,first_name,last_name,password=None):
        if not email:
            raise ValueError("Email must be there...")
        
        if not username:
            raise ValueError('username must be there...')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
       )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,first_name,last_name,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
            
        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_super_user=True


        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    first_name=m.CharField(max_length=50)
    last_name=m.CharField(max_length=50)
    username=m.CharField(max_length=50,unique=True)
    email=m.EmailField(max_length=254,unique=True)
    phone_number=m.CharField(max_length=10)

    #req 

    date_joined=m.DateTimeField(auto_now_add=True)
    last_joined=m.DateTimeField(auto_now_add=True)
    is_admin=m.BooleanField(default=False)
    is_staff=m.BooleanField(default=False)
    is_active=m.BooleanField(default=False)
    is_superuser=m.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects=MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True


