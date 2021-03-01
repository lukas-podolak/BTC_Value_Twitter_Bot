import tweepy
import cryptocompare
import json
import datetime

consumer_key = 'YOUR_KEY'
consumer_secret = 'YOUR_SECRET'
access_token = 'YOUR_TOKEN'
access_token_secret = 'YOUR_TOKEN_SECRET'

CRYPTOCOMPARE_API_KEY = 'YOUR_API_KEY'

cryptocompare.cryptocompare._set_api_key_parameter(CRYPTOCOMPARE_API_KEY)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

btc = cryptocompare.get_price('BTC', 'USD')
btc_dumps = json.dumps(btc)
btc_loads = json.loads(btc_dumps)

today = datetime.date.today()
today = today.strftime("%d.%m.%Y")

if datetime.datetime.now() < datetime.datetime.now().replace(hour=11,):
    print("[" + str(today) + "] #Bitcoin opened at " + str(btc_loads['BTC']['USD']) + " USD today.")
    api.update_status("[" + str(today) + "] #Bitcoin opened at " + str(btc_loads['BTC']['USD']) + " USD today.")
else:
    print("[" + str(today) + "] #Bitcoin value is " + str(btc_loads['BTC']['USD']) + " USD at the moment.")
    api.update_status("[" + str(today) + "] #Bitcoin value is " + str(btc_loads['BTC']['USD']) + " USD at the moment.")
