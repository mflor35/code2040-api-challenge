import json
import CODE2040API

def reversed_string(data,token):
    string         = json.loads(data)['result']
    reversed_str   = string[::-1]
    return {'token':token, 'string':reversed_str}

def main():
    my_token       = 'rmUQt128vF'
    challenge_data = CODE2040API.getchallenge(my_token,'http://challenge.code2040.org/api/getstring')
    answer_data    = reversed_string(challenge_data,my_token)
    validation     = CODE2040API.validatechallenge(answer_data,'http://challenge.code2040.org/api/validatestring')
    print "============== API response =================="
    print json.loads(validation)['result']
    #print answer_data
    CODE2040API.getGrades(my_token)
main()
