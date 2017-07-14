# import all the funcions in this function

from self_info import self_info
from select_a_username import select_a_username
from get_user_info import get_user_info
from like_user_post import like_user_post
from get_user_post import get_user_post
from post_a_comment import post_a_comment
from word_search_in_comment import word_search_in_comment
from get_list_of_comments import get_list_of_comments
from get_list_of_likes import get_list_of_likes
from delete_negative_comment import delete_negative_comment
from get_user_recent_post import get_user_recent_post
from get_own_recently_liked import get_own_recently_liked

#function starts the insta bot
def start_bot():

    self_info()
    print "Get a  particular user information"
    user_name = select_a_username()
    get_user_info(user_name)

    print"\n"
    choice = 'yes'
    while choice != 'no':
        print '\n'
        print "What would you like to do further?"
        print("1:To Like a post of your choice of the user.")
        print("2:To Comment on a post(not more than 200 words) of your choice of the user.")
        print("3:To Search a word in the comment in the post of your choice of the user.")
        print("4:To Get a list of comments on post of your choice of the user.")
        print("5:To Get a list of likes on post of your choice of the user.")
        print("6:To Delete the negative comment from a post of your choice of the user.")
        print("7:To Get your own recent post.")
        print("8:To Get the recent post of a user by username.")
        print("9:To Get your recently liked media.")
        print("10:To close the application.")
        print "\n"
        option = int(raw_input("Your option: "))
        print "cool.. plz wait..."
        if option not in range(1, 11):
            print"Invalid operation \nPlease try again!"
        elif option in range(1, 7):
            print "Which post you would wish to choose :"
            print "Press 1 for the one with the least popular."
            print "Press 2 for the one which has been uploaded recently. "
            print "Press 3 for the one which is the most popular."
            if option == 1:
                print "Press 4 to like all post"
            post_select = int(raw_input("Your option: "))
            print "loading.."
            if option == 1:
                user_name = select_a_username()
                if post_select in [1, 2, 3]:
                    like_user_post(user_name, option, post_select, 0)
                elif post_select == 4:
                    store = get_user_post(user_name)
                    length = len(store['data'])
                    for post in range(0, length):
                        n = post
                        like_user_post(user_name, option, 4, n)  # Here n is to give the post number.
                else:
                    print"Invalid post was chosen"
                    print" Sorry we have to perform the operation on the most recent post then"
            else:
                if post_select not in [1, 2, 3]:
                    print"Invalid post chosen \n"
            if option == 2:
                user_name = select_a_username()
                post_a_comment(user_name, option, post_select)
            if option == 3:
                user_name = select_a_username()
                word_search_in_comment(user_name, option, post_select)
            if option == 4:
                user_name = select_a_username()
                get_list_of_comments(user_name, option, post_select)
            if option == 5:
                user_name = select_a_username()
                get_list_of_likes(user_name, option, post_select)
            if option == 6:
                user_name = select_a_username()
                delete_negative_comment(user_name, option, post_select)
        if option == 7:
            user_name = select_a_username()
            get_user_recent_post(user_name)
        if option == 8:
            user_name = select_a_username()
            get_user_recent_post(user_name)
        if option == 9:
            get_own_recently_liked()
        if option == 11:
            print "Hope you had a good experience using instaBot"
            print "For any queries contact at :- chandelankit89@gmail.com"
            print "Thank You have a nice day!"
            exit()
        print "Do you want to continue?? (y/n)"
        opt = raw_input().upper()
        if opt == 'Y':
            choice = 'yes'
        elif opt == 'N':
            print "Hope you had a good experience using instaBot"
            print "For any queries contact at chandelankit89@gmail.com"
            print "Thank You have a nice day!"
            exit()
        else:
            print "Invalid choice"
            print "The program will shut down"
            print "THANK YOU"
            print "Hope you had a good experience using instaBot"
            print "For any queries contact at chndelankit89@gmail.com"
            print "Thank You have a nice day!"
            exit()
