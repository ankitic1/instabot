import requests
from constants import app_access_token,base_url

#self info function define
def self_info():
    request_url = (base_url + 'users/self/?access_token=%s') % (app_access_token)
    #https://api.instagram.com/v1/users/self/?access_token=APP_ACCESS_TOKEN
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()       # GET call to fetch self information
    
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            # Getting users full information.
            print('Full Name    : %s' % (user_info['data']['full_name']))
            print('Username     : %s' % (user_info['data']['username']))
            print('UserId       : %s' % (user_info['data']['id']))
            print('Followed By  : %s' % (user_info['data']['counts']['followed_by']))
            print('Follows      : %s' % (user_info['data']['counts']['follows']))
            print('Total Posts  : %s' % (user_info['data']['counts']['media']))

            if user_info['data']['website'] != '':      # Website of the user is given
                print('Website      :%s' % (user_info['data']['website']))
            else:
                print("website is not provided by user")
            if user_info['data']['bio'] != '':          # Bio of the user is given
                    print('Bio :%s' % (user_info["data"]["bio"]))
            else:
                print(" bio is not provided by user")


        else:
                print('User does not exist!',)
    else:
        print('Status code other than 200 received!')
