import random

# *in 10,000 times only 38 times coin show/is byesed*
print("*in 10,000 times only 38 times coin show/is byesed*") 
"""
def tossCoin():
    coinShows = random.randint(1,2)
    if coinShows == 1:
        print(coinShows,"You won this time.")
        return True
    else:
        print(coinShows,"You loos this time.")
        return False
"""
def rollDice():
    diceShow = random.randint(1,100)
    if diceShow == 100:
        print(diceShow, "Role was 100, you loos.What are the oods?!")
        return False
    elif diceShow <= 50:
        print(diceShow, "Role was <= 50, you loos")
        return False   
    else:
        print(diceShow, "Role was 100< role < 50, you won")     
        return True

def simple_bettor(funds, initial_wager, wager_count):   
    value = funds     
    wager = initial_wager
    current_wager = 0

    while current_wager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager
        current_wager += 1
    print("Funds: ", value)        

simple_bettor(1000,100,100)
a = int(input("Enter to exit..."))
