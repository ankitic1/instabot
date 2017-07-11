import requests
from search_post_by_choice import  search_post_by_choice
from constants import base_url,app_access_token

# Function to make a comment on a post of choice of the user
def post_a_comment(insta_username, option, post_selection):
    media_id = search_post_by_choice(insta_username, option, post_selection)
    url_post_comment = base_url + "media/" + media_id + "/comments"
    input_comment = raw_input("Write a comment you want to post.\n")
    request_data = {"access_token": app_access_token, 'text': input_comment}
    comment = requests.post(url_post_comment, request_data).json()  # POST call to comment the post
    if comment['meta']['code'] == 200:
        print ('Bravo.You successfully made a comment!')
    else:
        print('Your comment was unsuccessful. Try again!')