import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def get_oauth2_string(email, client_id, client_secret, refresh_token):
    creds = Credentials(
        None,
        refresh_token=refresh_token,
        token_uri='https://oauth2.googleapis.com/token',
        client_id=client_id,
        client_secret=client_secret
    )
    creds.refresh(Request())
    auth_string = f'user={email}\x01auth=Bearer {creds.token}\x01\x01'
    return base64.b64encode(auth_string.encode()).decode()
