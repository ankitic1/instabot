import requests
from constants import base_url,app_access_token
from get_user_id import get_user_id
# Function declaration to get the info of a user by username
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)       # Calling the function get_user_id to get a user_id
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (base_url + 'users/%s?access_token=%s') % (user_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()       # GET call to fetch user for the information
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            # Printing a particular user full information.
            print('Full Name    : %s' % (user_info['data']['full_name']))
            print('Username     : %s' % (user_info['data']['username']))
            print('UserId       : %s' % (user_id))
            print('Followed By  : %s' % (user_info['data']['counts']['followed_by']))
            print('Follows      : %s' % (user_info['data']['counts']['follows']))
            print('Total Posts  : %s' % (user_info['data']['counts']['media']))

            if user_info['data']['website'] != '':      # Website of the user is given
                print('Website      :%s' % (user_info['data']['website']))
            else:
                print"website is not provided by user"
            if user_info['data']['bio'] != '':           # Bio of the user is given
                print('Bio          :%s' % (user_info["data"]["bio"]))
            else:
                print"no bio found"
            print ("The user is a social bird")

        else:
            print('User does not exist!')
    else:
        print('Status code other than 200 received!')