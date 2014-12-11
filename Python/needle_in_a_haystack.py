import CODE2040API
import json
def findneedle(data,token):
    json_data      = json.loads(data)
    needle         = json_data['result']['needle']
    haystack       = json_data['result']['haystack']
    index          = 0

    for stuff in haystack:
        if needle == stuff:
            return {'token':token,'needle':index}
        index += 1


# Main or driving function
def main():
    my_token       = 'rmUQt128vF'
    challenge_data = CODE2040API.getchallenge(my_token,'http://challenge.code2040.org/api/haystack')
    answer_data    = findneedle(challenge_data,my_token)
    validation     = CODE2040API.validatechallenge(answer_data,'http://challenge.code2040.org/api/validateneedle')

    print "============== API response =================="
    print json.loads(validation)['result']
    CODE2040API.getGrades(my_token)
main()
