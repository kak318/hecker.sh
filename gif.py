import json
from urllib import parse, request

def get(q):
  url = "http://api.giphy.com/v1/gifs/search"

  params = parse.urlencode({
    "q": q,
    "api_key": "P7Uw28Z7VqjFR8YgD6kbYrpDNIxqYUKt",
    "limit": "1"
  })

  with request.urlopen("".join((url, "?", params))) as response:
    data = json.loads(response.read())

  print(json.dumps(data, sort_keys=True, indent=4))