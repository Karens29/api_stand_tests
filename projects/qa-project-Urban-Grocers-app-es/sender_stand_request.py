import configuration
import data
import requests

def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

def get_new_user_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers_with_auth
    )