import deck

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How many chips would like to bet? "))
        except:
            print("Sorry please provide an integer")
        
        else:
            if chips.bet >chips.total:
                print("Sorry you don't have enough chips! You have: {}".format(chips.total))
            
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 

    while True:
        x=input('Hit of Stand> Enter h or s')

        if x[0].lower() =='h':
            hit(deck,hand)
        
        elif x[0].lower == 's':
            print("Player Stands, Dealer's Turn")
            playing=False
        else:
            print("Sorry, I did not understand that. Please enter h or s only!")
            continue
        break