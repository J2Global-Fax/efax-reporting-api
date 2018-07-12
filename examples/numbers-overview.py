import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--date', help='Date to run report for: format YYYY-MM-DD', required=True)
parser.add_argument('--apikey', help="API Key provided", required=True)

parser.add_argument('--username', help='eFax Developer Username', required=True)
parser.add_argument('--password', help='eFax Developer Password', required=True)

args = parser.parse_args()

url = 'https://api.secure.efaxdeveloper.com/v1/number-overview/' + args.date

headers = {'x-api-key': args.apikey, 'efax-username': args.username, 'efax-password' : args.password}

r = requests.get(url, headers=headers)

parsed_json = json.loads(r.json())

for did in parsed_json:
   for username in parsed_json[did]:
      for fax_number in parsed_json[did][username]:
         print("for DID: {} and user {} to {} on {}:".format(did, username, fax_number, args.date))
         print("  Busy: {}".format(parsed_json[did][username][fax_number]['Busy']))
         print("  Call placement error: {}".format(parsed_json[did][username][fax_number]['Call placement error']))
         print("  Fax tranmission failed: {}".format(parsed_json[did][username][fax_number]['Fax transmission failed']))
         print("  No answer: {}".format(parsed_json[did][username][fax_number]['No answer']))
         print("  No dial tone: {}".format(parsed_json[did][username][fax_number]['No dial tone']))
         print("  Unspecified failure: {}".format(parsed_json[did][username][fax_number]['Unspecified failure']))
         print("  Success: {}".format(parsed_json[did][username][fax_number]['Success']))
         print("  Failures: {}".format(parsed_json[did][username][fax_number]['Failures']))
         print("  Total: {}".format(parsed_json[did][username][fax_number]['Total']))
         print("") 
