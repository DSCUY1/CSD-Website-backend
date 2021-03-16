import jwt
import datetime
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model
from rest_framework import exceptions


def access_tokens(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


class JwtAuthenticatedUser(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return None
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("unauthaticted")
        user = get_user_model().objects.filter(id=payload['user_id']).first()

        if user is None:
            raise exceptions.AuthenticationFailed(" user not Found ")
        return (user, None)