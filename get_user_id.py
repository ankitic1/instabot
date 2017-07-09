import requests
from constants import base_url,app_access_token
#       Function declaration to get the ID of a user by insta_username
def get_user_id(insta_username):
    request_url = (base_url + 'users/search?q=%s&access_token=%s') % (insta_username,app_access_token)
    #https://api.instagram.com/v1/users/search?q=insta_username&access_token=APP_ACCESS_TOKEN
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()       # GET call to fetch user for the information

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            user_id = user_info["data"][0]["id"]
            return user_id  # To Return user's id
        else:
            return None
    else:
        print('Status code other than 200 received!')