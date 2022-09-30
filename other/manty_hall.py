import random


"""
The Manty-Hall paradox is as follows:
1. There are TV-show, where there are 3 doors. Behind one of the doors there is a prize, but there is nothing behind the other doors.
2. The participant of the TV-show choices one of the three doors, then the host of the TV-show (who knows the door with the prize) opens one of the two doors (which are not selected by the participant), where there is no prize.
3. The participant has the opportunity to change the previous choice.
4. Will the chances of winning increase after changing the original choice?
"""

# create the list with door numbers
DOORS = [1, 2, 3]
# number of passes
NUM_PASSES = 10000
# initialize the winning door number with a random number
WIN_DOOR = random.choice(DOORS)

# create the dictionary with the number of wins for two particapants Alan and Po
# Alan does not change the original choise, but Po is the opposite
wins = {'Alan': 0, 'Po': 0}

# run a loop
for i in range(NUM_PASSES):
    # make the original choice
    original_choice = random.choice(DOORS)
    
    # create a set with door numbers and then remove from it the door from the original selection and the winning door (if they are different)
    set_for_open = set(DOORS)
    set_for_open.discard(original_choice)
    set_for_open.discard(WIN_DOOR)
    
    # select the door to open using a random.choice
    opened_door = random.choice(list(set_for_open))

    # Alan does not change the original choise
    alan_choice = original_choice

    # Po changes the initial selection
    set_to_choice = set(DOORS)
    set_to_choice.discard(original_choice)
    set_to_choice.discard(opened_door)
    po_choice = list(set_to_choice)[0]

    # counts the number of wins for each participant
    if alan_choice == WIN_DOOR:
        wins['Alan'] += 1
    if po_choice == WIN_DOOR:
        wins['Po'] += 1

print(f'Number of passes: {NUM_PASSES}')
print(f'Alan wins in {wins["Alan"]/NUM_PASSES*100} %')
print(f'Po wins in {wins["Po"]/NUM_PASSES*100} %')
