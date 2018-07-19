![eFaxDeveloper](https://secure.efaxdeveloper.com/efaxdev/img/developerLogo-sm.gif)

## Reporting API for efax Developer

This API provides 4 different reports for efax Developer Customers:

* Account Overview - Provides the failure reasons and counts for DID / Usernames for a specific account

* Number Overview - Provides the failure reasons and counts for DID / Usernames / Destination Numbers for an account for every combination that had at least one failure.

* Failures - Provides the failure reasons and counts for DID / Usernames /Destination Numbers for an account in which every attempt during a certain day failed.  These are users who were unable to send a successful fax to a specific number on a given day.

* Billable Pages - Pages sent by DID and account. 

## Access

All access requires an eFax Developer account and an API token.  Contact your sales rep to get registered for a token.

## Documentation

The API is documented via [swagger](swagger/eFaxDeveloperReportingAPI.json) and [html](docs/index.html)

There are four methods, each of which requires a date parameter in YYYY-MM-DD form:

* /account-overview/YYYY-MM-DD

* /number-overview/YYYY-MM-DD

* /failures/YYYY-MM-DD

* /billable-pages/YYYY-MM-DD

Every request requires 3 headers:

* x-api-key : API key provided to you.

* efax-username : your eFax Developer username

* efax-password : your eFax Developer Password

## Examples 

All examples are in the [examples](examples/) directory.

#### A Python sample:
```python
url = 'https://api.secure.efaxdeveloper.com/v1/number-overview/' + args.date

headers = {'x-api-key': args.apikey, 'efax-username': args.username, 'efax-password' : args.password}

r = requests.get(url, headers=headers)

parsed_json = json.loads(r.json())
```

#### result json:

```json
{
  "<DID 1>": {
    "user_1": {
      "<fax recipient 1>": {
        "Busy": 1,
        "Call placement error": 0,
        "Fax transmission failed": 0,
        "No answer": 0,
        "No dial tone": 0,
        "Unspecified failure": 0,
        "Success": 1,
        "Total": 2,
        "Failures": 1
      }
  }
```

## More Information
* [eFax Information](https://enterprise.efax.com/online-fax-services/fax-api)
* [eFax Developer Downloads](https://secure.efaxdeveloper.com/downloads.jsp)
* [eFax FAq's](http://www.efaxdeveloper.com/faq)

