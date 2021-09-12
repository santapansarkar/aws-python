import json
import os


def pets():
    my_pets={'kitten':'minu','puppie':'zomba','parrot':'ghungroo'}

    for keys,names in my_pets.items():
        if(keys == 'kitten'):
            print('My pet type {} and her name is {}'.format(keys,names))
            #print('My pets are {}'.format(names))
        elif(keys =='puppie'):
            print('My pet type {} and her name is {}'.format(keys,names))
        else:
            print('No pets are available now!')

def interaction():
    name = input('Hi, Thank you for running me !!!....What is your name?   ')
    print(f'Hi {name}...welcome to interaction chat!!!')
    if name.upper() == 'SRINIDHI':
        print(f'ohh you are puki...then why you are saying that you are {name}')
        response1 = input('AM i right? write yes or no  ')
        if response1.upper() == 'YES':
            print('See I got you!')
            print("Let's talk further...")
            response2 = input('Tell me who is your favourite author?  ')
            if response2.upper() == 'SUDHA MURTY':
                print(f'I knew that, you are a great fan of {response2}')
                response3 = input('Tell me Srinidhi, would you like to play Capital game with me? say yes or no  ')
                if response3.upper() == 'YES':
                    start_game()
    else:
        print('ummm.....I think you are hiding something from me!')
        print('since you are not telling me truth.....I will not play with you...Bye !!!')

def start_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'********************************')
    print(f'********************************')
    print(f'/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print(f'WELCOME TO CAPITAL GAME')
    print(f'/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print(f'*******************************')
    with open('list.json') as file_object:
        contents = json.load(file_object)
        no_rounds = input('how many rounds you want to play? write between 1 and 5 ')
        rounds = 0
        for rounds in range(int(no_rounds)):
            country_name = input('Please write name of any country[must be in proper case, e.g. India]   ')
            for item in contents:
                if country_name == item['country']:
                    print(f"Here is my answer, Capital of {country_name} is {item['city']}")
                    rounds = int(rounds)+1

           
               # print(f'Here is the capital of {country_name} - {item[city]}')

# print(type(item))
# for dict_val in item:

if __name__ == '__main__':
    interaction()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'********************************')
    print(f'********************************')
    print('Thank you for playing with me Srinidhi, bye bye ...pou pou....bye bye !!!')
   #start_game()