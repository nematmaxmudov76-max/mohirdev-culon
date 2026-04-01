from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class MyBasicAuth(BaseAuthentication):
    def authenticate(self, request):
        return super().authenticate(request)

    def authenticate_credentials(self, userid, password, request=None):

        if userid != settings.ONEID_USERNAME:
            raise exceptions.AuthenticationFailed(
                "Authentication failed. Wrong username."
            )
        if password != settings.ONEID_PASSWORD:
            raise exceptions.AuthenticationFailed(
                "Authentication failed. Wrong password."
            )

        return (True, None)
