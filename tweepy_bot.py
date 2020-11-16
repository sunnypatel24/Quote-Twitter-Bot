import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("x8CBkKLvPLThzoAwtv9raepAf",
"Dyyxq8tt36WpLXXNhBQBg6v9rwgIo3xqG03hroCIuAFo5KWvsN")
auth.set_access_token("1327826996462841856-Tfr9gzDWwRJhAWIp6LsKoRtACAxEGF",
"rYox2DZ7N3NLsZ3lrxNapL87d3uKODxFPr60I2oekqLZ5")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
