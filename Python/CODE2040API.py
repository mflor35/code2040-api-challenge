import urllib2
import json

def register(email,github):
    url     = 'http://challenge.code2040.org/api/register'
    values  = { 'email': email, 'github':github}
    req     = urllib2.Request(url)
    req.add_header('Content-Type', 'Application/json')
    rsp    = urllib2.urlopen(req, json.dumps(values))
    content = rsp.read()

    return content

#  getchallenge takes in a token and url and returns a sring with the challenge data
def getchallenge(token,url):
    info           = {'token':token}
    request        = urllib2.Request(url)
    request.add_header('Conten-Type', 'application/json')
    response       = urllib2.urlopen(request, json.dumps(info))
    content        = response.read()
    return content

# Validatechallenge() takes in a json string with the answer for the challenge and url
def validatechallenge(answer_dict,url):
    request        = urllib2.Request(url)
    request.add_header('Conten-Type','application\json')
    response       = urllib2.urlopen(request,json.dumps(answer_dict))
    content        = response.read()
    print ""
    print "------- API response-------------- "
    return json.loads(content)['result']

def getGrades(token):
    info           = {'token':token}
    request        = urllib2.Request('http://challenge.code2040.org/api/status')
    request.add_header('Conten-Type', 'application/json')
    response       = urllib2.urlopen(request, json.dumps(info))
    content        = response.read()
    result         = json.loads(content)['result']
    print
    print "============== Grades ========================"
    for challenge in sorted(result.keys()):
        print challenge + '\t\t' + str(result[challenge])
