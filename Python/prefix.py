
def prefix(data,token):
    result         = json.loads(data)['result']
    array          = result['array']
    prefix         = result['prefix']
    new_array      = []

    for stuff in array:
        if stuff.find(str(prefix)) < 0:
            new_array.append(stuff)

    return {'token':token,'array':new_array}

def main():
    my_token       = 'rmUQt128vF'
    challenge_data = getchallenge(my_token,'http://challenge.code2040.org/api/prefix')
    answer_data    = prefix(challenge_data,my_token)
    validation     = validatechallenge(answer_data,'http://challenge.code2040.org/api/validateprefix')
    print "============== API response =================="
    print json.loads(validation)['result']
    getGrades(my_token)
main()
