import requests
from constants import base_url,app_access_token
from get_user_id import get_user_id

# The function below fetches all public post starting from the most recent one published by the user using 'GET'.
def get_user_post(username):
    user_id = get_user_id(username)  # get_user_id(username) function called here to get the user's ID
    user_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
    request_user_recent_post = requests.get(user_url).json()  # GET call to fetch user's post
    return request_user_recent_post
