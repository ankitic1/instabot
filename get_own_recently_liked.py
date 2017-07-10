import requests
from constants import base_url,app_access_token
import  urllib


#  Get the list of recent media liked by the owner of id
def get_own_recently_liked():
    request_url = (base_url + 'users/self/media/liked/?access_token=%s') % (app_access_token)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            if own_media['data'][0]['caption'] != 'None':
                print("Caption:"),
                print (own_media['data'][0]['caption']['text'])
                print("Image Name:"),
                print image_name
            else:
                print("Image Name"),
                print image_name
            print('Your image has been downloaded!')
        else:
            print('Post does not exist!')
    else:
        print('Status code other than 200 received!')