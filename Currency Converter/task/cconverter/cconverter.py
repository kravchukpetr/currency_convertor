# write your code here!
import json
import requests

cached_list = ['eur', 'usd']
input_currency = input()
url = "".join(['http://www.floatrates.com/daily/', input_currency.lower(), '.json'])
r = requests.get(url)
json_dict = json.loads(r.text)
with open('cache_file.json', 'w') as cache_json:
    json.dump({k: v for k, v in json_dict.items() if k in cached_list}, cache_json)
while True:
    exchange_currency = input()
    if exchange_currency == "":
        break
    amount_money = float(input())
    print('Checking the cache...')
    with open('cache_file.json', 'r') as cache_json:
        json_from_dict = json.load(cache_json)
    if exchange_currency.lower() in json_from_dict.keys():
        print('Oh! It is in the cache!')
        print(f"You received {round(amount_money * json_from_dict[exchange_currency.lower()]['rate'], 2)} {exchange_currency.upper()}.")
    else:
        print('Sorry, but it is not in the cache!')
        cached_list.append(exchange_currency.lower())
        r = requests.get(url)
        json_dict = json.loads(r.text)
        with open('cache_file.json', 'w') as cache_json:
            json.dump({k: v for k, v in json_dict.items() if k in cached_list}, cache_json)
        print(f"You received {round(amount_money * json_dict[exchange_currency.lower()]['rate'], 2)} {exchange_currency.upper()}.")






