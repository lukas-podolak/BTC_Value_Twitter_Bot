import tweepy
import cryptocompare
import json
import datetime

consumer_key = 'qrfpYT0rivTSnmOwRr9NAVrxs'
consumer_secret = 'njjYuQKVva06ng5aOTBXlhgg44wAaUYyTEaBwKrKUsUiRPVt2D'
access_token = '1359229309647540225-H5998lkbtY5h9vqWEqhhYEYHRZhmch'
access_token_secret = '9Pn04JM9cAYpt7Dv9Zhtjz1H3yIYthJNSM3se6RRQ5mMt'

CRYPTOCOMPARE_API_KEY = 'ad5247330a6468b2e6eb4d86618f3b05bdf30b7492ac6b5b8fb6bfcb0dee21df'

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