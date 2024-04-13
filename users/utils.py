import re
import requests
from django.conf import settings

def get_refresh_token(refresh_token):
    
    refresh_url = settings.REFRESH_URL
    
    data={
        'refresh_token': refresh_token
    }
    
    response = requests.post(refresh_url, data=data)
    
    if response.status_code == 200:
        # Extract the new access token from the response
        new_access_token = response.json().get('access_token')
        return new_access_token
    else:
        # Token refresh failed, return None
        return None
    
def is_valid_email(email):
    # Define the regex pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Use re.match to check if the email matches the pattern
    return re.match(pattern, email) is not None
