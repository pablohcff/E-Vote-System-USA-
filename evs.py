import os

def clear_screen(): ### function to clear the screen as we interact with the output 
    os.system('cls' if os.name == 'nt' else 'clear')

id_electors_section = [000, 333, 666, 999] ### stores the ID of that section's electors, (predefined)
already_voted = []

number_trump = 1
number_kamala = 2
number_kennedy = 3

votes_trump = 0
votes_kamala = 0
votes_kennedy = 0

def show_results(): ### function created to show this section's results

    clear_screen()

    total_votes = votes_trump + votes_kamala + votes_kennedy

    if total_votes == 0:
        print("There's 0 (zero) votes registered, returning to main menu...")
        main_menu()

    print("Here's this section's results: ")
    print(f'Candidate Trump (1): {(votes_trump / total_votes) * 100:.2f}%  - votes: [{votes_trump}]')
    print(f'Candidate Kamala (2): {(votes_kamala / total_votes) * 100:.2f}% - votes: [{votes_kamala}]')
    print(f'Candidate Kennedy (3): {(votes_kennedy / total_votes) * 100:.2f}% - votes: [{votes_kennedy}]')

    if votes_trump > votes_kamala and votes_trump > votes_kennedy:
        print("\n Trump is this section's winner.")
    elif votes_kamala > votes_trump and votes_kamala > votes_kennedy:
        print("\n Kamala is this section's winner.")
    elif votes_kennedy > votes_trump and votes_kennedy > votes_kamala:
        print("\n Kennedy is this section's winner.")
    else:
        print("There's no winner.")
    
    exit()

def vote_section(): ### function created to confirm the vote to a candidate

    clear_screen()

    global votes_trump, votes_kamala, votes_kennedy
    
    print("\nNow, you just need to vote!\n")
    vote_insert = int(input("Insert your candidate's number: "))
   
    if vote_insert == 1:

        clear_screen()

        print("\n Here's your candidate's info: ")
        print("\n Trump, number: 1. \n Republican.")
        confirm_vote = input('\nDo you confirm this vote? (Y/N): ')
       
        if confirm_vote == "Y" or confirm_vote == "y":
            print("\n Vote confirmed.")
            votes_trump += 1
            main_menu()
        else:
            print("\n Wrong option? Try again: \n")
            vote_section()
        
    elif vote_insert == 2:

        clear_screen()

        print("\n Here's your candidate's info: ")
        print("\n Kamala, number: 2. \n Democrat.")
        confirm_vote = input('Do you confirm this vote? (Y/N): ')
       
        if confirm_vote == "Y" or confirm_vote == "y":
            print("\n Vote confirmed.")
            votes_kamala += 1
            main_menu()
        else:
            print("\n Wrong option? Try again: \n")
            return vote_section()
    
    elif vote_insert == 3:
        clear_screen()
        print("\n Here's your candidate's info: ")
        print("\n Kennedy, number: 3. \n Democrat.")
        confirm_vote = input('Do you confirm this vote? (Y/N): ')
       
        if confirm_vote == "Y" or confirm_vote == "y":
            print("\n Vote confirmed.")
            votes_kennedy += 1
            main_menu()
        else:
            print("\n Wrong option? Try again: \n")
            return vote_section()
        
    else:
        print("\n There's no candidate associated to it, try again.")
        return vote_section()

def vote_option(): ### function created to initiate the vote option, checking if the elector is able to vote or not.

    clear_screen()

    print("\n Let's just check if you're able to vote")
   
    check_id = int(input("\n Insert your ID number: "))
   
    if check_id in id_electors_section and check_id not in already_voted: ### checks if the elector is part of that section or if he has already voted
        print("\n You're able to vote.")
        already_voted.append(check_id) ### Stores that elector in the list to make sure he cannot vote again
        vote_section()
       
    else:
        print("\n You're NOT able to vote or already voted")
        main_menu()

def main_menu(): ### function created to show the main menu

    print("\n***Welcome to Electronic Voting System***\n")
    print("\n Here's the options: ")
    print("1. Vote")
    print("2. Show EVS results")
    menu_option = int(input("\n Insert your option: "))
   
    if menu_option == 1:
        vote_option()
    elif menu_option == 2:
        show_results()
    else:
        print("Invalid option.")
        main_menu()

while True:
    main_menu()