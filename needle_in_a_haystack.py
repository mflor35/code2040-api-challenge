import urllib2
import json
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
    return content

# Start of solution to the challenge
def findneedle(data):
    json_data      = json.loads(data)
    needle         = json_data['result']['needle']
    haystack       = json_data['result']['haystack']
    index          = 0

    for stuff in haystack:
        if needle == stuff:
            return {'token':'rmUQt128vF','needle':index}
        index += 1
# End of solution to the challenge

# Main or driving function
def main():
    my_token       = 'rmUQt128vF'
    challenge_data = getchallenge(my_token,'http://challenge.code2040.org/api/haystack')
    answer_data    = findneedle(challenge_data)
    validation     = validatechallenge(answer_data,'http://challenge.code2040.org/api/validateneedle')
    print json.loads(validation)['result']
main()
