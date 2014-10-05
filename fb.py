
import facebook

 


import requests

from time import strftime

AFTER = "1392891447"
import time

import json

token=""#Insert access token here.  



graph1 = facebook.GraphAPI(token)


profile = graph1.get_object("me")
friends = graph1.get_connections("me", "friends")
graph1.put_object("me", "feed", message="I am writing on my wall!")
tags = json.dumps([{'x':50, 'y':50, 'tag_uid':12345}, {'x':10, 'y':60, 'tag_text':'a turtle'}])
graph1.put_photo(open('Your photo in the same folder'), 'Look at this cool photo!', None, tags=tags)

#Gets the posts on your wall

def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""

    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
    "filter_key = 'others' AND source_id =me()  AND "
    "created_time > " + AFTER + " LIMIT 200")

    payload = {'q': query, 'access_token': token}

    r = requests.get('https://graph.facebook.com/fql', params=payload)

    result = json.loads(r.text)

    return result

#print get_posts()


#Get posts in a group
#data = graph1.get_object("Group id" + "/feed", page=False, retry=50, limit=800000000)
#print data

# Comment on a post in a group
#graph1.put_object("Id of the post in the group", "comments", message="hehe")




#r = requests.get('https://graph.facebook.com/%s' % wallpost['actor_id'])

#Comments on all the wall posts
def commentall(wallposts):
    """Comments thank you on all posts"""




    for wallpost in wallposts:
        r = requests.get('https://graph.facebook.com/%s' %
        wallpost['actor_id'])
        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
        user = json.loads(r.text)
        #message = 'Thanks %s :)' % user['first_name']
        message = 'Thanks %s :)'
        payload = {'access_token': token, 'message': message}

        s = requests.post(url, data=payload)
        print s

        print "Wall post %s done" % wallpost['post_id']


graph1.put_object("Id of the page you own", "feed", message="I am writing on my wall!")'''

