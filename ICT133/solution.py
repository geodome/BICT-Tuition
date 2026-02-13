"""
Pseudocode and Python code for Q1(a)
"""

def round_up(foot_length:float) -> float:
    """
    Round up foot length to nearest 0.5cm

    input: foot_length(cm)
    output: round up foot_length

    floor = max integer <= foot_length
    for example, the floor of 3.2 is 3.

    if foot_length == floor or foot_length == floor + 0.5 then
        return foot_length
    else if foot_length - foot < 0,5 then
        return floor + 0.5
    else
        return floor + 1
    
    """
    floor = int(foot_length)
    if foot_length == floor or foot_length == floor + 0.5:
        return foot_length
    elif foot_length - floor < 0.5:
        return floor + 0.5
    else:
        return floor + 1    
    
def q1a() -> None:
    """
    input: gender (M or F), foot length (cm)
    output: shoe size

    gender = ask user for gender
    foot length = ask user for foot size

    round up foot length to nearest 0.5cm

    # what are the conditions for custom shoe?
    if foot length > 29.5 or foot length < 21.1 then
        print "Call Customer Service for Custom-made Shoe"
    else
        # what are the conditions to use the female shoe size table?
        if (user is female and 21.5 <= foot length <= 26) or (user is male and foot length < 24) then
            shoe size = foot length - 17
            print f"US Female {shoe size}"

        # What are the conditions to use the male shoe size table?
        else if (user is male and 24 <= foot length <= 29.5) or (user is female and foot size > 26) then
            shoe size = foot size - 18
            print f"US Male {shoe size}"

        # in case of unaccounted error
        else
            print "Unknown shoe size"

    """

    gender = input("Enter gender (M/F): ").upper()
    foot_length = float(input("Enter foot length (cm): "))

    foot_length = round_up(foot_length)

    if foot_length > 29.5 or foot_length < 21.1:
        print("Call Customer Service for Custom-made Shoes")
    else:
        if (gender == "F" and 21.5 <= foot_length <= 26) or (gender == "M" and foot_length < 24):
            shoe_size = foot_length - 17
            print(f"US Female {shoe_size}")
        elif (gender == "M" and 24 <= foot_length <= 29.5) or (gender == "F" and foot_length > 26):
            shoe_size = foot_length - 18
            print(f"US Male {shoe_size}")
        else:
            print("Unknown shoe size")

"""
Pseudocode and Python Code for Q3(c)
"""

import random

def enter_player_list() -> list[str]:
    """
    input: players' names
    output: a list of players with at least 2 players and no duplicate names

    player_list = []
    while True:
        enter player's name
        if user hits enter:
            if there are at least 2 players then
                return player_list
            else
                print "at least 2 players"
        else if player's name is unique then
            append player's name to player_list
        else:
            print "player's name is duplicate
    """
    unique_names = []
    players = []
    while True:
        player = input("Enter player: ").strip()
        if player == "":
            if len(players) >= 2:
                return players 
            else:
                print("Mininum 2 players.")
        if player.lower() not in unique_names:                    
            unique_names.append(player.lower())
            players.append(player)
        else:
            print("No duplicate names. Re-enter.")

def enter_hand_size() -> int:
    """
    input: hand_size
    output: hand_size must be even and greater than 3

    hand_size = 0
    while hand_size is not valid
        hand_size = ask user for hand size
    return hand_size
    """
    hand_size = 0
    while not (hand_size > 3 and hand_size %2 == 0):
        hand_size = int(input("Enter hand size: ") )
    return hand_size

def create_hands(players:list[str], hand_size:int) -> list[list[int]]:
    """
    input: player list, hand_size
    output: a list of player's hand
    
    hands = []
    for each player
        create hand of given hand size
        append hand to hands
    return hands
    """
    hands = []
    for p in players:
        hand = []
        for i in range(hand_size):
            hand.append(random.randint(0,9))
        hands.append(hand)
    return hands

def is_correct(expression:str) -> bool:
    """
    Check if expression is correct format
    input: expression is a string
    output: True if the expression is correct, else False

    A correct expression has a length of 3
    first character is a digit 0-0
    last character is a digit 0-9
    the 2nd character is either + or -
    """
    return len(expression) == 3 and expression[0].isdigit() and expression[2].isdigit() and expression[1] in ["+", "-"]

def matches(expression:str, result:int) -> bool:
    """
    input: expression, result
    output: true if the evaluated expression value is the same as result, else false

    d1 = extract first digit from expression
    d2 = extract last digit from expression
    operator = extract operator from expression

    if there is wildcard 0 then
        return True
    else if operator is + then
        return d1 + d2 == result 
    else
        return d1 - d2 == result
    """
    d1 = int(expression[0])
    d2 = int(expression[2]) 
    operator = expression[1]
    if 0 in [d1, d2]:
        return True
    elif operator == "+":
        return d1 + d2 == result 
    else:
        return d1 - d2 == result

def remove_from_hand(hand:list[int], expression:str) -> bool:
    """
    input: hand, expression
    output: True is expression was removed from hand, else False

    d1 = extract 1st digit from expression
    d2 = extract 2nd digit from expression

    if d1 and d2 are same digit then
        if hand contains at least 2 d1 then
            remove d1 from hand
            remove d1 from hand 
            return True 
    else 
        if hand contains at 1east 1 d1 and at least 1 d2 then
            remove d1 from hand
            remove d2 from hand
            return True 
    
    return False
    """
    d1 = int(expression[0])
    d2 = int(expression[2])

    if d1 == d2:
        if hand.count(d1) >= 2:
            hand.remove(d1)
            hand.remove(d1)
            return True
    else:
        if hand.count(d1).count >= 1 and hand.count(d2) >= 1:
            hand.remove(d1)
            hand.remove(d2)
            return True 
        
    return False


def q3a() -> None:
    """
    enter player list
    enter player hand size
    shuffle player list

    for each game
        create new hand for each player
        
        round_no = 0
        for each round
            round_no += 1
            result = random digit 0 to 9
            print f"round {round number}: Result {result}"

            for each player
                print player's hand

                player enters expression
                if player enters skipped then
                    print "skipped"
                else if player enters incorrect expression then
                    print "incorrect"
                else if expression matches result then
                    remove cards from player's hand
                    if removed successfully then
                        print "correct"
                        if player's hand is empty then
                            print f"{player name} wins in {round number} rounds"
                            game over
                    else
                        print f"{player}'s hand does not contain {expression}"
                else
                    print "Unknown outcome"
                
                print player's hand
    """

    players = enter_player_list()
    random.shuffle(players)
    hand_size = enter_hand_size()

    game_over = False
    while not game_over:
        hands = create_hands(players, hand_size)

        round_number = 0
        next_round = True 
        while next_round:
            round_number += 1

            result = random.randint(1,9)
            print(f"Round {round_number}: Result {result}")

            for p in range(len(players)):
                player = players[p]
                print(f"{player}'s hand: {hands[p]}")

                expression = input("Enter expression: ").strip()

                if expression == "":
                    print("Skipped")
                elif not is_correct(expression):
                    print("Incorrect!")
                elif matches(expression, result):
                    removed = remove_from_hand(hands[p], expression)
                    if removed:
                        print("Correct!")
                        if len(hands[p]) == 0:
                            print(f"{player} wins in {round_number} rounds")
                            game_over = True 
                            next_round = False 
                            break
                    else:
                        print(f"{player}'s hand does not contain {expression}")
                else:
                    print("Unknown outcome")
                
                print(f"{player}'s hand: {hands[p]}")
