import requests

# Set up game constants
deck_count = 1
base_url = 'https://deckofcardsapi.com/api/deck/'
deck_url = f'{base_url}new/shuffle/?deck_count={deck_count}'
hit_url = f'{base_url}<<deck_id>>/draw/?count=1'

# Start game
print('Welcome to Blackjack!')

# Shuffle the deck and get the deck ID
response = requests.get(deck_url)
data = response.json()
deck_id = data['deck_id']

# Function to get the value of a card
def get_card_value(card):
    if card in ['KING', 'QUEEN', 'JACK']:
        return 10
    elif card == 'ACE':
        return 11
    else:
        return int(card)


while True:
    # Draw the player's first two cards
    response = requests.get(hit_url.replace('<<deck_id>>', deck_id))
    player_cards = [response.json()['cards'][0]['value']]
    response = requests.get(hit_url.replace('<<deck_id>>', deck_id))
    player_cards.append(response.json()['cards'][0]['value'])

    # Draw the dealer's first card
    response = requests.get(hit_url.replace('<<deck_id>>', deck_id))
    dealer_cards = [response.json()['cards'][0]['value']]

    # Keep track of scores
    player_score = sum([get_card_value(card) for card in player_cards])
    dealer_score = get_card_value(dealer_cards[0])

    # Print initial hands
    print(f'Your hand: {player_cards} ({player_score})')
    print(f"Dealer's hand: {dealer_cards} ({dealer_score})\n")

    # Player's turn
    while player_score < 21:
        choice = input("Do you want to hit or stand? Type 'h' or 's': ")
        if choice.lower() == 'h':
            response = requests.get(hit_url.replace('<<deck_id>>', deck_id))
            new_card_value = response.json()['cards'][0]['value']
            player_cards.append(new_card_value)
            player_score += get_card_value(new_card_value)
            print(f'Your hand: {player_cards} ({player_score})')
        elif choice.lower() == 's':
            break

    # Determine winner
    if player_score > 21:
        print('You busted! Dealer wins.')
    else:
        while dealer_score < 17:
            response = requests.get(hit_url.replace('<<deck_id>>', deck_id))
            new_card_value = response.json()['cards'][0]['value']
            dealer_cards.append(new_card_value)
            dealer_score += get_card_value(new_card_value)

        print(f"Dealer's hand: {dealer_cards} ({dealer_score})")
        if dealer_score > 21:
            print('Dealer busted! You win.')
        elif dealer_score > player_score:
            print('Dealer wins!')
        elif player_score > dealer_score:
            print('You win!')
        else:
            print('It\'s a tie!')

    # Ask if the player wants to play again
    play_again = input('Do you want to play again? Type \'y\' or \'n\': ')
    if play_again.lower() == 'n':
        print('Thanks for playing! Goodbye.')
        break
