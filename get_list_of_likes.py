import requests
from search_post_by_choice import search_post_by_choice
from constants import base_url,app_access_token


#   Function to get the list of likes on a post of choice
def get_list_of_likes(insta_username, option, post_selection):
    media_id = search_post_by_choice(insta_username, option, post_selection)
    request_url = (base_url+ 'media/%s/likes?access_token=%s') % (media_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    like_list = requests.get(request_url).json()
    if like_list['meta']['code'] == 200:
        if len(like_list['data']):
            for x in range(0, len(like_list['data'])):
                print(like_list['data'][x]['username'])
        else:
            print("There was no like found.")
    else:
        print("Status code other than 200 received.")
