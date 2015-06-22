try:
    import tweepy
except Exception, e:
    print "Please install tweepy : pip install tweepy"

class TwitterAnalysis:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret


        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)


    def find_not_follow(self, user_name):
        followers = [user.screen_name for user in tweepy.Cursor(self.api.followers, screen_name=user_name).items()]
        following = [user.screen_name for user in tweepy.Cursor(self.api.friends, screen_name=user_name).items()]

        following_followers = list(set(following) - set(followers))


        print "###################################################################### \n" \
              "#### You are following this users. But they aren't following you. #### \n" \
              "###################################################################### \n"

        counter = 0
        for user in following_followers:
            print "{0}. {1}".format(counter, user)
            counter += 1

    def find_not_following(self, user_name):
        followers = [user.screen_name for user in tweepy.Cursor(self.api.followers, screen_name=user_name).items()]
        following = [user.screen_name for user in tweepy.Cursor(self.api.friends, screen_name=user_name).items()]

        followers_following = list(set(followers) - set(following))

        print "####################################################################### \n" \
              "#### You aren't following this users. But they aren following you. #### \n" \
              "####################################################################### \n"

        counter = 0
        for user in followers_following:
            print "{0}. {1}".format(counter, user)
            counter += 1