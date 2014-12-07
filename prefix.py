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
def prefix(data,token):
    result         = json.loads(data)['result']
    array          = result['array']
    prefix         = result['prefix']
    new_array      = []
    
    for stuff in array:
        if stuff.find(str(prefix)) < 0:
            new_array.append(stuff)

    return {'token':token,'array':new_array}
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
    challenge_data = getchallenge(my_token,'http://challenge.code2040.org/api/prefix')
    answer_data    = prefix(challenge_data,my_token)
    validation     = validatechallenge(answer_data,'http://challenge.code2040.org/api/validateprefix')
    print "============== API response =================="
    print json.loads(validation)['result']
    getGrades(my_token)
main()
