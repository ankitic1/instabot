from get_user_post import  get_user_post


# Search the one which is most popular least popular and the recent one.
def search_post_by_choice(insta_username, option=0, post_selection=0, n=0):
    search_post = get_user_post(insta_username)      # This function is called here to get the user's post details.
    post_index = 0  # For most recent post
    like_on_a_post = []
    comment_on_a_post = []
    total_media = len(search_post['data'])             # To get the total no. of media
    if total_media == 0:
        print("This User has no footprints on instagram:-(!")
    else:
        if option == 1:  # For liking a post
            for each_media in range(0, total_media):
                like_on_a_post.append(search_post['data'][each_media]['likes']['count'])
            if post_selection == 1:  # If we want least popular post to be liked
                least_count = min(like_on_a_post)
                post_index = like_on_a_post.index(least_count)
            if post_selection == 2: # If we want recent post to be liked
                post_index = 0
            if post_selection == 3:  # If we want most popular post to be liked
                most_count = max(like_on_a_post)
                post_index = like_on_a_post.index(most_count)
            if post_selection == 4:
                post_index = n
        if option == 2 or 3 or 4 or 5 or 6:  # For commenting on a post
            for each_media in range(0, total_media):
                comment_on_a_post.append(search_post['data'][each_media]['comments']['count'])
            if post_selection == 1:  # If we want to commented on least popular post
                least_count = min(comment_on_a_post)
                post_index = comment_on_a_post.index(least_count)
            if post_selection == 2:  # If we want recent post to be commented
                post_index = 0
            if post_selection == 3:  # If we want to comment on most popular post
                most_count = max(comment_on_a_post)
                post_index = comment_on_a_post.index(most_count)
        print "Link to the Media        :", search_post['data'][post_index]['link']  # To print the link to a media.
        media_id = search_post["data"][post_index]['id']
        return media_id  # To return the particular media ID
