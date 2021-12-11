from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, phone, password, is_staff, **extra_fields):
        if not phone:
            raise ValueError('User must have phone number')
        if not password:
            raise ValueError('User must have password')

        user = self.model(phone=phone, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        return self._create_user(phone, password, is_staff=False, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        return self._create_user(phone, password, is_staff=True, **extra_fields)
