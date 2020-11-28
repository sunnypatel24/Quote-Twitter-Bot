from urllib.request import urlopen
url = "http://www.quotationspage.com/random.php"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode('utf-8')

start_index = html.find('<dt class=\"quote\"><a title=\"Click for further information about this quotation\" href=\"/quote/')
quote_start = start_index + len('<dt class=\"quote\"><a title=\"Click for further information about this quotation\" href=\"/quote/')
quote_end = html.find('</a> </dt>')
raw_quote = html[quote_start:quote_end]
quote = ""
#raw_quote = raw_quote.partition('html">')
print(raw_quote)

#print(quote)









#import tweepy

# Authenticate to Twitter
#auth = tweepy.OAuthHandler("sMoA8AXezVoU0N8VZBp7kU9GQ",
#"S3yQYThATrfnfgRucbQsK6qIq1SGFDDlabQE6ERG0cvlUBP6Fg")
#auth.set_access_token("1327826996462841856-oujiUKbB4Dj3giY13EzUNlctLb6A6p",
#"bWiyTozNLf95Dp2iJChGNoNJC30qCJUd7aYVBjkBlpcTw")

#api = tweepy.API(auth)

#try:
#    api.verify_credentials()
#    print("Authentication OK")
#except:
#    print("Error during authentication")

#api.update_status("Test tweet from Tweepy Python")

#api.update_profile(description="A random quote bot")
