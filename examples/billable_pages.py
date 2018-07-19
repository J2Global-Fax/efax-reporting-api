import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--date', help='Date to run report for: format YYYY-MM-DD', required=True)
parser.add_argument('--apikey', help="API Key provided", required=True)

parser.add_argument('--username', help='eFax Developer Username', required=True)
parser.add_argument('--password', help='eFax Developer Password', required=True)

args = parser.parse_args()

url = 'https://api.secure.efaxdeveloper.com/v1/billable-pages/' + args.date

headers = {'x-api-key': args.apikey, 'efax-username': args.username, 'efax-password' : args.password}

r = requests.get(url, headers=headers)

print(r.json())
parsed_json = json.loads(r.json())

for did in parsed_json:
   for username in parsed_json[did]:
      print("for DID: {} and user {} on {}:".format(did, username, args.date))
      for resolution in parsed_json[did][username]:
         print("  Resolution: {}".format(parsed_json[did][username][resolution]))
