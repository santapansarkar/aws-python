def poll_func():
    poll_continue = True
    poll_dict = {}    
    while poll_continue:
        name = input("\nWhat is your name? ")
        poll_response = input("\nWhat is your favorite color? ")
        poll_dict[name] = poll_response
        poll_continue = input("\nWould you like to continue? (y/n) ")
        if poll_continue == "n":
            poll_continue = False
    for key,values in poll_dict.items():
        print(f"{key}'s favorite color is {values}.")

def main():
    poll_func()
if __name__ == "__main__":
    main()
