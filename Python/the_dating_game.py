import iso8601 # Needs to be installed in the system before running the script.
import datetime # http://pyiso8601.readthedocs.org/en/latest/#parsed-formats
import json
import CODE2040API

def datingGame(data,token):
    result         = json.loads(data)['result']
    datestamp      = result['datestamp']
    interval       = result['interval']
    time           = iso8601.parse_date(datestamp)
    time           = time + datetime.timedelta(seconds=interval)
    return {'token':token, 'datestamp':str(time.isoformat())}

def main():
    my_token       = 'rmUQt128vF'
    challenge_data = CODE2040API.getchallenge(my_token,'http://challenge.code2040.org/api/time')
    answer_data    = datingGame(challenge_data,my_token)
    validation     = CODE2040API.validatechallenge(answer_data,'http://challenge.code2040.org/api/validatetime')
    print "============== API response =================="
    print json.loads(validation)['result']
    #print answer_data
    CODE2040API.getGrades(my_token)
main()
