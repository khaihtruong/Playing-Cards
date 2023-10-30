"""
   CS5001 - Fall 2023

   Khai Truong

   cards.py

   Three different function include
   create_deck() - create a deck of 52 cards
   shuffle(cards) - shuffle a deck of card
   deal(number_of_hands, number_of_cards, cards) -
   deal a set of cards given number of hands and cards in each hands
"""
# import random function
import random

def create_deck():
    '''
    FUNCTIONS - create_deck()
    Create a deck of 52 cards using abbreviation outlined

    PARAMETERS
    None

    RETURN
    A list of card not shuffle
    '''
    # list of first character
    number = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    # list of second character
    face = ['s', 'h', 'd', 'c']

    # combine first character and second character
    deck = [f'{a}{b}'for a in number for b in face]
    return deck

def shuffle(cards):
    '''
    FUNCTION - shuffle(cards)
    shuffle a deck of given cards
    
    PARAMETER
    cards - set of cards that want to be shuffle
    
    RETURN
    a list of shuffled cards. (the original list is not modified)
    '''
    # make a copy of the original list
    new_list = cards.copy()

    # make mutated list
    mutated_list = []

    # for loop the amount of cards in a deck
    for i in range(len(new_list)):

        # since list start counting at 0, the count will need to adjust by 1
        count_adjustment = 1
        
        # randomize for a number between zero and number of cards
        i = random.randint(0, len(new_list) - count_adjustment)

        # take the randomize card out the list
        random_pick = new_list.pop(i)

        # append the randomize card into the mutated list
        mutated_list.append(random_pick)
    
    # return the mutated list
    return mutated_list

def deal(number_of_hands, number_of_cards, cards):
    '''
    FUNCTION - shuffle(cards)
    shuffle a deck of given cards
    
    PARAMETER
    cards - set of cards that want to be shuffle

    PRECONDITIONS
    number of cards has been pre-validated, values allowed: 0..13;
    number of hands has been pre-validated, values allowed: 1..4
    
    RETURN
    a list of shuffled cards. (the original list is not modified)
    '''
    # shuffle the list of cards
    shuffle(cards)
    
    # number of hands is 4, make a finish list with 4 sublist
    if number_of_hands == 4:
        finish_deck = [[], [], [], []]

        # run the loops same amount as the number of cards
        for i in range(number_of_cards):

            # append a character into the finish deck
            finish_deck[0].append(cards.pop(0))
            finish_deck[1].append(cards.pop(0))
            finish_deck[2].append(cards.pop(0))
            finish_deck[3].append(cards.pop(0))

        # return the list of hands and the remaining cards
        return finish_deck
    
    # number of hands is 3, make a finish list with 3 sublist
    elif number_of_hands == 3:
        finish_deck = [[], [], []]

        # run the loops same amount as the number of cards
        for i in range(number_of_cards):

            # append a character into the finish deck
            finish_deck[0].append(cards.pop(0))
            finish_deck[1].append(cards.pop(0))
            finish_deck[2].append(cards.pop(0))
            
        # return the list of hands
        return finish_deck

    # number of hands is 2, make a finish list with 2 sublist
    elif number_of_hands == 2:
        finish_deck = [[], []]

        # run the loops same amount as the number of cards
        for i in range(number_of_cards):

            # append a character into the finish deck
            finish_deck[0].append(cards.pop(0))
            finish_deck[1].append(cards.pop(0))
            
        # return the list of hands and the remaining cards
        return finish_deck

    # number of hands is 1, make a finish list with 1 sublist
    else:
        finish_deck = [[]]
        
        # run the loops same amount as the number of cards
        for i in range(number_of_cards):

            # append a character into the finish deck
            finish_deck[0].append(cards.pop(0))
            
        # return the list of hands, original deck is the leftover
        return finish_deck
