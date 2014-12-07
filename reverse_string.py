#Stage I: Rervese a string
import urllib2
import json
#Connect to the API and get challenge
challenge_url  = 'http://challenge.code2040.org/api/getstring'
info           = {'token':'rmUQt128vF'}
request        = urllib2.Request(challenge_url)
request.add_header('Conten-Type', 'application/json')

response       = urllib2.urlopen(request, json.dumps(info))
content        = response.read()

# Reverse the string given by the API
string         = json.loads(content)['result']
reversed_str   = string[::-1]

#submit reversed string to the API
submit_url     = 'http://challenge.code2040.org/api/validatestring'
info           = {'token':'rmUQt128vF', 'string':reversed_str}
request        = urllib2.Request(submit_url)
request.add_header('Conten-Type','application\json')
response       = urllib2.urlopen(request,json.dumps(info))
content        = response.read()
print content
