import urllib2
import json
url     = 'http://challenge.code2040.org/api/register'
values  = { 'email': 'floresmigu3l@gmail.com', 'github':'https://github.com/mflor35/code2040-api-challenge'}
req     = urllib2.Request(url)
req.add_header('Content-Type', 'Application/json')

rsp    = urllib2.urlopen(req, json.dumps(values))
content = rsp.read()

print content
