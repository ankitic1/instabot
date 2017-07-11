import requests
from constants import base_url,app_access_token
from search_post_by_choice import search_post_by_choice
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


# Function declaration to make delete negative comments from the recent post
def delete_negative_comment(insta_username,option,post_select):
    media_id = search_post_by_choice(insta_username, option, post_select)
    request_url = (base_url+ 'media/%s/comments/?access_token=%s') % (media_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            # Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (base_url + 'media/%s/comments/%s?access_token=%s') % (
                        media_id, comment_id, app_access_token)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'