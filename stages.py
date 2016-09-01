import iso8601  # Needs to be installed first
import datetime  # http://pyiso8601.readthedocs.org/en/latest/#parsed-formats
import json
import pprint


def prefix(data, token):
    """@data: contains the json string with the prefix and array
       @token: string with token to authenticate to API"""
    print()
    print("** Solving Prefix **")
    print("++++++++++++++++++++++++++++++++++++++++++")
    pprint.pprint(data)
    print("+++++++++++++++++++++++++++++++++++++++++++")
    result = json.loads(data)
    array = result['array']
    prefix = result['prefix']
    new_array = []
    print("Array: ", array)
    print("Prefix: ", prefix)

    for stuff in array:
        if(stuff.find(prefix) < 0):
            new_array.append(stuff)

    print("Array of Strings without the given prefix")
    return {'token': token, 'array': new_array}


def findneedle(data, token):
    """@data: contains the json string with the prefix and array
       @token: string with user token to authenticate to API"""
    print()
    print("** Finding needle **")
    json_data = json.loads(data)
    needle = json_data['needle']
    haystack = json_data['haystack']
    index = 0
    print("Needle => ", needle)
    print("Haystack => ", haystack)
    for stuff in haystack:
        if needle == stuff:
            print("Index =>", index)
            return {'token': token, 'needle': index}
        index += 1


def reverse_string(data, token):
    """@data: contains the json string with the prefix and array
       @token: string with user token to authenticate to API"""
    print()
    print("** Reversing String **")
    string = data
    reversed_str = string[::-1]
    print("String =>", string)
    print("Reversed =>", reversed_str)
    return {'token': token, 'string': reversed_str}


def datingGame(data, token):
    """@data: contains the json string with the prefix and array
       @token: string with user token to authenticate to API"""
    print()
    print("** Calculating date **")
    result = json.loads(data)
    datestamp = result['datestamp']
    interval = result['interval']
    time = iso8601.parse_date(datestamp)
    time = time + datetime.timedelta(seconds=interval)
    print("Datestamp => ", datestamp)
    print("Interval => ", interval)
    return json.JSONEncoder().encode({'token': token, 'datestamp': str(time.isoformat())})
