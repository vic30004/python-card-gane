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


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! PUSH")


while True:
    # Print an opening statement

    print("WELCOME TO BLACKJACK")
    # Create and shuffle the deck, deal two cards to each player
    decks = deck.Deck()
    decks.shuffle()

    player_hand = deck.Hand()
    player_hand.add_card(decks.deal())
    player_hand.add_card(decks.deal())

    dealer_hand = deck.Hand()
    dealer_hand.add_card(decks.deal())
    dealer_hand.add_card(decks.deal())

    # Set up the player's chips
    player_chips = deck.Chips()

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one delaer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # this is being called from the hit_or_stand func

        # Prompt for player to hit or stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceedss 21, run player_bust() and break out the loop
        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

        # If player hasn't buster, player Dealer's hand until Dealer reacher 17
        if player_hand.value <=21:
            while dealer_hand.value<player_hand.value:
                hit(deck,dealer_hand)
            #show all cards
            show_all(player_hand,dealer_hand)
            # Run different winning scenaris
            if dealer_hand.value >21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value >player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value <player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
        # Inform Player of their chips total
        print('\n Player total chips are at: {}'.format(player_chips.total))
        # Ask to play again 
        new_game = input("Would you like to play another hand? y/n")

        if new_game[0].lower() =='y':
            playing=True
            continue
        else:
            print('Thank you for playing! Hope you had a good time.')
            break