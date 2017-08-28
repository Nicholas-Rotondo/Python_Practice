import pynder
import itertools
import config


### Validate session ###
session = pynder.Session(config.FBID, config.FACEBOOK_AUTH_TOKEN)

### Grabs list of users
users = session.nearby_users()

### If she only has one photo, or no bio return dislike
### If she likes art superlike
### else like
def criteria(user):
    bio = user.bio
    if len(user.photos) == 1 or bio == None:
        return 0
    elif "art" in bio:
        return 1
    else:
        return 2

### Like, dislike or superlike
def like_or_not(users):
    likes = session.likes_remaining
    if likes == 0:
        return "try again later"
    else:
        for user in itertools.islice(users, likes):
            crit = criteria(user)
            if crit == 0:
                print user.dislike()
            elif crit == 1:
                print user.superlike()
            else:
                print user.like()

while True:
    like_or_not(users)
