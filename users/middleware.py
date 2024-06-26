import datetime
from typing import Any
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from users.utils import get_refresh_token

class TokenRefreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            expiry_time = getattr(user, 'expiry_time', None)  # Assuming your token has an expiry time attribute
            if expiry_time:
                # Check if the access token is about to expire
                if expiry_time <= timezone.now() + datetime.timedelta(minutes=5):
                    # Token is about to expire, refresh it
                    new_access_token = get_refresh_token(getattr(user, 'refresh_token', None))
                    if new_access_token:
                        # Update the access token in the user object
                        setattr(user, 'access_token', new_access_token)
                    else:
                        # Failed to refresh token, return unauthorized response
                        return Response({"error": "Failed to refresh access token"}, status=status.HTTP_401_UNAUTHORIZED)

        response = self.get_response(request)
        return response