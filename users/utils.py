import requests

def get_refresh_token(refresh_token):
    
    refresh_url = 'http://127.0.0.1:8000/user/token/refresh'
    
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