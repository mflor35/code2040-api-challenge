import urllib2
#url     = 'http://challenge.code2040.org/api/register'
#values  = { 'email': 'floresmigu3l@gmail.com', 'github':'https://github.com/mflor35/code2040-api-challenge'}
#data    = urllib.urlencode(values)
url     = 'http://www.voidspace.org.uk'
req     = urllib2.Request(url)
rsp     = urllib2.urlopen(req)

content = rsp.read()

print content
