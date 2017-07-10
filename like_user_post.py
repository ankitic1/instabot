import requests
from constants import base_url,app_access_token
from search_post_by_choice import search_post_by_choice
# Function to like a users post by choice

def like_user_post(insta_username, option, post_selection, n):
    media_id = search_post_by_choice(insta_username, option, post_selection,n)
    like_post_url = base_url + "media/" + media_id + "/likes"
    payload = {'access_token': app_access_token}
    like = requests.post(like_post_url, payload).json()  # POST call to like the post
    if like['meta']['code'] == 200:
        print ('Bravo,Like was successful!')
    else:
        print('Your like was unsuccessful. Try again!')