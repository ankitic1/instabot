import requests
from search_post_by_choice import search_post_by_choice
from constants import base_url,app_access_token
#  Function to get the list of comments on a post

def get_list_of_comments(insta_username, option, post_selection):
    media_id = search_post_by_choice(insta_username, option, post_selection)
    request_url = base_url + "media/" + media_id + "/comments?access_token=%s" %app_access_token
    print 'GET request url : %s' % (request_url)
    comment_list = requests.get(request_url).json()
    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
                for x in range(0,len(comment_list['data'])):
                    print(comment_list['data'][x]['from']['username']+": "),
                    print(comment_list['data'][x]['text'])
        else:
            print("There was no comment found.")
    else:
        print("Status code other than 200 received.")