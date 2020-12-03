from urllib.request import urlopen
import tweepy

# Web scrape from a quotes website to get a quote and the author

url = "http://www.quotationspage.com/random.php"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode(encoding='cp1252')
start_index = html.find('<dt class=\"quote\"><a title=\"Click for further information about this quotation\" href=\"/quote/')
quote_start = start_index + len('<dt class=\"quote\"><a title=\"Click for further information about this quotation\" href=\"/quote/')
quote_end = html.find('</a> </dt>')
raw_quote = html[quote_start:quote_end]
quote = ""
is_angle = False
for c in raw_quote:
    if not is_angle:
        pass
    if c == '>':
        is_angle = True
        continue
    if is_angle:
        quote += c
author_start_index = html.find('<b><a href=')
author_start = author_start_index + 20
author_end = html.find('</a>] </div>')
raw_author = html[author_start:author_end]
author = "- "
for a in raw_author:
    if a == '_':
        author += ' '
        continue
    elif a == '/':
        break
    else:
        author += a



tweet = quote + "\n" + author


# Open a text file to write the quote into, and later tweet the quote from
with open("quotes.txt", "w") as file:
    file.write(tweet)

# Authenticate to Twitter

auth = tweepy.OAuthHandler(consumer_key,
consumer_secret)
auth.set_access_token(token_key,
token_secret)

api = tweepy.API(auth)


# Try to tweet a quote, print if it succeeded or failed
try:
    with open("quotes.txt", "r") as file:
        api.update_status(file.read())
    print("Success")
except:
    print("Fail")
