import CODE2040API
import json


def main():
    my_token       = 'rmUQt128vF'
    challenge_data = CODE2040API.getchallenge(my_token,)
    answer_data    = prefix(challenge_data,my_token)
    validation     = CODE2040API.validatechallenge(answer_data,'http://challenge.code2040.org/api/validateprefix')
    print "============== API response =================="
    print json.loads(validation)['result']
    CODE2040API.getGrades(my_token)
main()
