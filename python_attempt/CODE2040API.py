import requests  # Installation required
import json


def register(registration_url, token, github):

    values = {'token': token, 'github': github}
    rsp = requests.post(registration_url, data=values)
    content = rsp.text
    return content


def getchallenge(token, url):
    info = {'token': token}
    rsp = requests.post(url, data=info)
    content = rsp.text
    return content


def validatechallenge(answer_dict, url):
    rsp = requests.post(url, data=answer_dict)
    content = rsp.text
    return content


def status(url, token):
    info = {'token': token}
    rsp = requests.post(url, data=info)
    content = rsp.text
    result = json.loads(content)
    print()
    print("** STATUS **")
    for challenge in sorted(result.keys()):
        print(challenge + '\t\t' + str(result[challenge]))
