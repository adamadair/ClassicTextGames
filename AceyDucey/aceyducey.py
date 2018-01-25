import random


# This is a faithful port of aceyducey.bas to Python.

def intro():
    # 10 - 80
    print(tab(26) + "ACEY DUCEY CARD GAME")
    print(tab(15) + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n\n")
    print("ACEY-DUCEY IS PLAYED IN THE FOLLOWING MANNER ")
    print("THE DEALER (COMPUTER) DEALS TWO CARDS FACE UP")
    print("YOU HAVE AN OPTION TO BET OR NOT BET DEPENDING")
    print("ON WHETHER OR NOT YOU FEEL THE CARD WILL HAVE")
    print("A VALUE BETWEEN THE FIRST TWO.")
    print("IF YOU DO NOT WANT TO BET, INPUT A 0")


def run():
    dollars = 100
    while dollars > 0:
        print("YOU NOW HAVE {0} DOLLARS\n".format(dollars))  # 120
        cards = [random.randint(2, 14), random.randint(2, 14)]
        while cards[0] == cards[1]:
            cards[1] = random.randint(2, 14)
        a = min(cards)
        b = max(cards)
        print(" " + get_card(a))
        print(" " + get_card(b))
        print()
        m = get_bet(dollars)
        if m > 0:
            c = random.randint(2, 14)
            print(" " + get_card(c))
            if a < c < b:
                print("YOU WIN!!!")
                dollars += m
            else:
                print("SORRY, YOU LOSE")
                dollars -= m

        else:
            print("CHICKEN!!\n")


def get_bet(d):
    while True:
        try:
            m = int(input("WHAT IS YOUR BET? "))
            if m > d:
                print("SORRY, MY FRIEND, BUT YOU BET TOO MUCH.")
                print("YOU HAVE ONLY {0} DOLLARS TO BET.".format(d))
            return m
        except:
            pass


def get_card(c):
    if c < 11:
        return str(c)
    elif c == 11:
        return "JACK"
    elif c == 12:
        return "QUEEN"
    elif c == 13:
        return "KING"
    elif c == 14:
        return "ACE"
    raise Exception("Unknown card value: " + str(c))


def tab(t):
    return " " * t


if __name__ == '__main__':
    # this part bootstraps the program and catches and exceptions
    # and allows the user to ctrl-c out of the program.
    try:
        intro()
        run_me = True
        while run_me:
            run()
            print("\n\nSORRY, FRIEND, BUT YOU BLEW YOUR WAD.\n\n")
            run_me = input("TRY AGAIN (YES OR NO)? ").upper() == "YES"
        print("O.K., HOPE YOU HAD FUN!")
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print(err)
