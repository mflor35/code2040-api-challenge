import iso8601 # Needs to be installed in the system before running the script.
import datetime # http://pyiso8601.readthedocs.org/en/latest/#parsed-formats
import json
import CODE2040API

def prefix(data,token):
    print "------------------------------"
    print "Prefix"
    print "------------------------------"

    result         = json.loads(data)['result']
    array          = result['array']
    prefix         = result['prefix']
    new_array      = []
    print "Array: ", array
    print "Prefix: ", prefix

    for stuff in array:
        if stuff.find(str(prefix)) < 0:
            new_array.append(stuff)
    print "Array of Strings without the given prefix"
    print new_array
    return {'token':token,'array':new_array}

def findneedle(data,token):
    json_data      = json.loads(data)
    needle         = json_data['result']['needle']
    haystack       = json_data['result']['haystack']
    index          = 0

    for stuff in haystack:
        if needle == stuff:
            return {'token':token,'needle':index}
        index += 1

def reversed_string(data,token):

    print "--------------------------"
    print "Reversed String Challenge"
    print "--------------------------"

    string         = json.loads(data)['result']
    reversed_str   = string[::-1]
    print "String: ", string
    print "Reversed String: ", reversed_str
    return {'token':token, 'string':reversed_str}

def datingGame(data,token):
    result         = json.loads(data)['result']
    datestamp      = result['datestamp']
    interval       = result['interval']
    time           = iso8601.parse_date(datestamp)
    time           = time + datetime.timedelta(seconds=interval)
    return {'token':token, 'datestamp':str(time.isoformat())}
