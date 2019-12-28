import deck

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would like to bet? "))
        except:
            print("Sorry please provide an integer")

        else:
            if chips.bet > chips.total:
                print("Sorry you don't have enough chips! You have: {}".format(
                    chips.total))

            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit of Stand> Enter h or s')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower == 's':
            print("Player Stands, Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that. Please enter h or s only!")
            continue
        break

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! PUSH")


while True:
    # Print an opening statement

    print("WELCOME TO BLACKJACK")
    # Create and shuffle the deck, deal two cards to each player


    # Set up the player's chips


    # Prompt the player for their bet

    # Show cards (but keep one delaer card hidden)


    while playing: #this is being called from the hit_or_stand func

        # Prompt for player to hit or stand

        # Show cards (but keep one dealer card hidden)

        # If player's hand exceedss 21, run player_bust() and break out the loop

