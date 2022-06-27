from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.core.mail import send_mail

class CustomUser(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email must cannot be empty')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8)

    objects = CustomUser()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self) -> str:
        return self.email

    def has_module_perms(self, app_label: str) -> bool:
        return self.is_staff

    def has_perm(self, obj) -> bool:
        return self.is_staff

    
   

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='followers', on_delete=models.SET_NULL, null=True)
    follow = models.ForeignKey(User, related_name='follows', on_delete=models.SET_NULL, null=True)
    is_follow = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user} -> {self.follow}'
