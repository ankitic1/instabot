# Getting the list of sandbox users to perform action
from sandbox_users import users
# Function to select a username fron sandbox users
def select_a_username():
    # To select a user
    print ("This is the list.Choose a username and have fun :-)")
    for ele in users:
        print (ele)
    # Select the user_name of the user
    insta_username = raw_input("Enter the Username: ")
    if insta_username not in users:
        print "Sorry this user is not present"
        print "Please select a valid user to perform action"
        select_a_username()
    else:
        return insta_username

