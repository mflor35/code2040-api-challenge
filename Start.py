import stages
import json
import CODE2040API
# Main or driving function
def main():
    my_token       = 'rmUQt128vF'

    challenge_urls = [
            'http://challenge.code2040.org/api/getstring',
            'http://challenge.code2040.org/api/prefix',
            'http://challenge.code2040.org/api/time',
            'http://challenge.code2040.org/api/haystack',
            ]

    validation_urls= [
            'http://challenge.code2040.org/api/validatestring',
            'http://challenge.code2040.org/api/validateprefix',
            'http://challenge.code2040.org/api/validatetime',
            'http://challenge.code2040.org/api/validateneedle'
            ]

    valid_choice = True
    while(valid_choice == True):
        print "******************************************"
        print "Select Challenge to be solved:           *"
        print "1.- Reverse String                       *"
        print "2.- Prefix                               *"
        print "3.- The Dating Game                      *"
        print "4.- Haystack                             *"
        print "                                         *"
        print "Enter 'Grades' to check grade on the API *"
        print "******************************************"
        user_choice = raw_input("Enter choice: ")

        if user_choice == '1':
            challenge_data   = CODE2040API.getchallenge(my_token,challenge_urls[0])
            challenge_answer = stages.reversed_string(challenge_data,my_token)
            print CODE2040API.validatechallenge(challenge_answer,validation_urls[0])

        elif user_choice == '2':
            challenge_data   = CODE2040API.getchallenge(my_token,challenge_urls[1])
            challenge_answer = stages.prefix(challenge_data,my_token)
            print CODE2040API.validatechallenge(challenge_answer,validation_urls[1])

        elif user_choice == '3':
            challenge_data   = CODE2040API.getchallenge(my_token,challenge_urls[2])
            challenge_answer = stages.datingGame(challenge_data,my_token)
            print CODE2040API.validatechallenge(challenge_answer,validation_urls[2])

        elif user_choice == '4':
            challenge_data   = CODE2040API.getchallenge(my_token,challenge_urls[3])
            challenge_answer = stages.findneedle(challenge_data,my_token)
            print CODE2040API.validatechallenge(challenge_answer,validation_urls[3])
        elif user_choice.lower() == 'grades':
            CODE2040API.getGrades(my_token)
        else:
            valid_choice = False
main()
