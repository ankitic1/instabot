import requests
from constants import base_url,app_access_token
import urllib
from get_user_id import get_user_id

# Function declaration to get the recent post of a user by username
def get_user_recent_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (base_url+ 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()       # GET call to fetch the user recent post

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            if user_media['data'][0]['caption']['text'] != '':
                print("Caption:"),
                print (user_media['data'][0]['caption']['text'])
                print("Image Name:"),
                print image_name
            else:
                print("Image Name"),
                print image_name
            print('The post has been downloaded!')
        else:
            print('Post does not exist!')
    else:
        print('Status code other than 200 received!')
