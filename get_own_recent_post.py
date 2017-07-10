import  requests
from constants import*
import urllib
# Function declaration to get recent post of yourself
def get_own_recent_post():
    #  https://api.instagram.com/v1/users/self/media/recent/?access_token=APP_ACCESS_TOKEN
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (app_access_token)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()           # GET call to fetch details of own recent post

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            # urlib used for retreiving the post and downloading it.
            urllib.urlretrieve(image_url, image_name)
            if own_media['data'][0]['caption']['text'] != '':
                # If caption is present successfully printing caption along with image.
                print("Caption:"),
                print (own_media['data'][0]['caption']['text'])   # Fetching the caption of the post
                print("Image Name:"),
                print image_name
            else:
                # Only image fetched as no caption present.
                print("Image Name"),
                print image_name
            print('The post has been downloaded!')
        else:
            print('Post does not exist!')
    else:
        print('Status code other than 200 received!')