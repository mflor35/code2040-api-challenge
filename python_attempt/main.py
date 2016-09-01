#! /bin/python3
import stages
import CODE2040API


def find_solution(url, data, token):

    if(url.find('reverse') > 0):
        return stages.reverse_string(data, token)
    elif(url.find('haystack') > 0):
        return stages.findneedle(data, token)
    elif(url.find('prefix') > 0):
        return stages.prefix(data, token)
    elif(url.find('dating') > 0):
        return stages.datingGame(data, token)
    return -1


def main():
    registration_url = 'http://challenge.code2040.org/api/register'
    status_url = 'http://challenge.code2040.org/api/status'
    token = '174f74259da7236f9a2011c1c0b68511'
    steps_urls = [
        'http://challenge.code2040.org/api/reverse',
        'http://challenge.code2040.org/api/haystack',
        'http://challenge.code2040.org/api/prefix',
        'http://challenge.code2040.org/api/dating'
    ]

    validation_urls = [
        'http://challenge.code2040.org/api/reverse/validate',
        'http://challenge.code2040.org/api/haystack/validate',
        'http://challenge.code2040.org/api/prefix/validate',
        'http://challenge.code2040.org/api/dating/validate',
    ]

    print("Solving Challenges")

    for i in range(0, len(steps_urls)):
        data = CODE2040API.getchallenge(token, steps_urls[i])
        solution = find_solution(steps_urls[i], data, token)
        if(solution != -1):
            print(solution)
            print(CODE2040API.validatechallenge(solution, validation_urls[i]))
        else:
            print("solution not found")

    print(CODE2040API.status(status_url, token))
main()
