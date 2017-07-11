import requests
from search_post_by_choice import search_post_by_choice
from constants import base_url,app_access_token


#  The Function gives Id of a comment that contains a particular word in a particular post
def word_search_in_comment(insta_username,option,post_select):
    media_id = search_post_by_choice(insta_username, option, post_select)  # search_post_by_choice(username) function called here to get post ID
    url_post_comment = base_url + "media/" + media_id + "/comments?access_token=" + app_access_token
    all_comments = requests.get(url_post_comment).json()
    search_word = raw_input("Enter a word you want to search in the comments")
    print "\n<>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<>"
    comments_id = []
    list_of_comments = []
    user_name = []
    for each_comment in all_comments['data']:
        list_of_comments.append(each_comment['text'])
        comments_id.append(each_comment['id'])
        user_name.append(each_comment['from']['username'])
    comments_id_matched = []
    comments_matched = []
    user_found = []
    for each_item in range(len(list_of_comments)):  # Search for the comment that contains the specified word
        if search_word in list_of_comments[each_item]:
            comments_matched.append(list_of_comments[each_item])
            comments_id_matched.append(comments_id[each_item])
            user_found.append(user_name[each_item])
    if len(comments_matched) == 0:  # No comment Found with the word you searched
        print "No comment have word:" + search_word
        return False, media_id, False
    else:  # Comment found with word search!
        print "These comments contains the word:" + search_word
        for i in range(len(comments_matched)):
            print(">>>>>>> " + comments_matched[i])
        return comments_id_matched, media_id, comments_matched
