import termcolor
from logic import *

mustard = Symbol("mustard")
plum = Symbol("plum")
scarlet = Symbol("scarlet")
peacock = Symbol("peacock")
white = Symbol("white")
green = Symbol('green')
characters = [mustard, plum, scarlet, peacock, white, green]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
billard = Symbol("ballroom")
study= Symbol("study")
dining = Symbol("dining")
lounge = Symbol("lounge")
hall = Symbol("hall")
conservatory = Symbol("conservatory")
rooms = [ballroom, kitchen, library, billard, study, dining, lounge, hall, conservatory]

knife = Symbol("knife")
revolver = Symbol("revolver")
spanner = Symbol("spanner")
candle = Symbol("candlestick")
rope = Symbol("rope")
pipe = Symbol("leadpipe")
weapons = [knife, revolver, spanner, candle, rope, pipe]

symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet, peacock, white, green),
    Or(ballroom, kitchen, library, billard, study, dining, lounge, hall, conservatory),
    Or(knife, revolver, spanner, candle, rope, pipe)
)

# check_knowledge(knowledge)

# turn counter
i=0

init_symbols = []

while(True):
    # Get Initial cards
    init_cards = input("Enter your initial cards seperate with a space : ").split(' ')
    invalid_cards = []

    for init_card in init_cards:
        register = False

        for symbol in symbols:
            if symbol.name == init_card:
                init_symbols.append(symbol)
                register = True
                break

        if not register: invalid_cards.append(init_card)   #Catch invalid card entry
    
    if len(invalid_cards) != 0:
        print("The following entries are invalid:")
        for invalid_card in invalid_cards:
            print(invalid_card)

    else: break


for symbol in init_symbols:
    knowledge.add(Not(symbol))


while (True):
    print('Type "1" for your guess')
    print('Type "2" for someone else guess')
    input_type = int(input('Whose guess : '))
    # For your guess certain knowledge
    if input_type == 1:
        guessed_symbols = []
        while(True):
            guessed_cards = input("Enter your guessed cards seperate with a space : ").split(' ')
            invalid_cards = []

            for guessed_card in guessed_cards:
                register = False

                for symbol in symbols:
                    if symbol.name == guessed_card:
                        guessed_symbols.append(symbol)
                        register = True
                        break

                if not register: invalid_cards.append(guessed_card)   #Catch invalid card entry

            if len(invalid_cards) != 0:
                print("The following entries are invalid:")
                for invalid_card in invalid_cards:
                    print(invalid_card)

            else: break
        
        for symbol in guessed_symbols:
            knowledge.add(Not(symbol))

    elif input_type == 2:
        guessed_symbols = []
        while(True):
            guessed_cards = input("Enter other's guessed cards seperate with a space : ").split(' ')
            invalid_cards = []

            for guessed_card in guessed_cards:
                register = False

                for symbol in symbols:
                    if symbol.name == guessed_card:
                        guessed_symbols.append(symbol)
                        register = True
                        break

                if not register: invalid_cards.append(guessed_card)   #Catch invalid card entry

            if len(invalid_cards) != 0:
                print("The following entries are invalid:")
                for invalid_card in invalid_cards:
                    print(invalid_card)

            elif len(guessed_symbols) != 3:
                print("Invalid amount of guessed card")

            else: break
        
        knowledge.add(Or(
            Not(guessed_symbols[0]), guessed_symbols[1], guessed_symbols[2]
        ))  


    check_knowledge(knowledge)


