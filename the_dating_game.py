import urllib2
import json
import iso8601 # Needs to be installed in the system before running the script.
import datetime # http://pyiso8601.readthedocs.org/en/latest/#parsed-formats

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
def datingGame(data,token):
    result         = json.loads(data)['result']
    datestamp      = result['datestamp']
    interval       = result['interval']
    time           = iso8601.parse_date(datestamp)
    time           = time + datetime.timedelta(seconds=interval)
    return {'token':token, 'datestamp':str(time.isoformat())}
# End of solution to the challenge
def getGrades(token):
    info           = {'token':token}
    request        = urllib2.Request('http://challenge.code2040.org/api/status')
    request.add_header('Conten-Type', 'application/json')
    response       = urllib2.urlopen(request, json.dumps(info))
    content        = response.read()
    result         = json.loads(content)['result']
    print "============== Grades ========================"
    for challenge in result:
        print challenge + '\t\t' + str(result[challenge])

# Main or driving function
def main():
    my_token       = 'rmUQt128vF'
    challenge_data = getchallenge(my_token,'http://challenge.code2040.org/api/time')
    answer_data    = datingGame(challenge_data,my_token)
    validation     = validatechallenge(answer_data,'http://challenge.code2040.org/api/validatetime')
    print "============== API response =================="
    print json.loads(validation)['result']
    #print answer_data
    getGrades(my_token)
main()
