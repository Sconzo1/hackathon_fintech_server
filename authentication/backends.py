from django.contrib.auth.backends import ModelBackend
from django.utils import timezone

from authentication.models import User


class PhoneAuthBackend(ModelBackend):
    def authenticate(self, request=None, phone=None, password=None, username=None, **kwargs):
        if not phone:
            phone = username
        if not (phone and password):
            return None
        try:
            user = User.objects.get(phone=phone)
            if user.check_password(password):
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                return user
        except User.DoesNotExist:
            return None
