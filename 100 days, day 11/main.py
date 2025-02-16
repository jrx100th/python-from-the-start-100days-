## Day 11 Goal : Black Jack
"""import random


computer1 = (random.randint(8,10))
computer2 = (random.randint(8,10))

computer_list = []

computer_list.append(computer1)
computer_list.append(computer2)

print(f"These are the computers cards {computer_list}")

print(f"This is the sum of the cards of the computer : {sum(computer_list)}")

user_list = [random.randint(1,10), random.randint(1,10)]

print(f"These are your current cards {user_list}")
print(f"This is the sum of your cards {sum(user_list)}")

print("Do you think you can add one more card and get the black jack by defeating the computer")

user_choice = input("Type 'yes' if you can or 'no' if you want to end the game now :")

if user_choice == "yes":
    user_list.append(random.randint(1,10))

    print(f"Now you're total cards are {user_list}")
    print(f"And it totals to {sum(user_list)}")
    if sum(user_list) <= 21:
        print("Congrats You Won")
    else:
        print("You lost better luck next time")
else :
    if sum(user_list) <= 21:
        print("Congrats You Won")
    else:
        print("You lost better luck next time")"""

import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Face cards count as 10, Ace as 11
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the score for a given hand."""
    score = sum(cards)
    if score > 21 and 11 in cards:  # Convert Ace (11) to (1) if needed
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def compare(player_score, dealer_score):
    """Compares final scores to determine the winner."""
    if player_score > 21:
        return "You busted! Dealer wins."
    elif dealer_score > 21:
        return "Dealer busted! You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score == 21 and len(player_cards) == 2:
        return "Blackjack! You win!"
    elif dealer_score == 21 and len(dealer_cards) == 2:
        return "Dealer has Blackjack! You lose."
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "Dealer wins."


# Game Start
while True:
    print("\nWelcome to Blackjack!\n")

    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
            break

        hit_or_stay = input("Type 'h' to hit, 's' to stay: ").lower()
        if hit_or_stay == 'h':
            player_cards.append(deal_card())
        else:
            game_over = True

    # Dealer plays if player hasn't busted
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    print(compare(player_score, dealer_score))

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break
