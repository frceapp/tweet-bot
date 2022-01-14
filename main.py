import tweepy, time

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    api.update_status_with_media(status="update server status :", filename="neko.png")
    time.sleep(14400)