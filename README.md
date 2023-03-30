# Blackjack-
README: Import Requests for Blackjack Game

This is a simple implementation of a Blackjack game using Python's requests module to make HTTP requests to the Deck of Cards API. This implementation draws two cards for the player and one card for the dealer to begin the game. The player can then decide to hit or stand while attempting to get as close to 21 points as possible. The dealer will continue to draw cards until they have a score of at least 17. The game will then determine a winner based on the highest score without going over 21.

Installation
This implementation requires the requests module. You can install it using pip:

Copy code
pip install requests
Usage
To start the game, run the blackjack.py script. The game will begin with a welcome message, and the deck will be shuffled to obtain a deck ID from the Deck of Cards API. The game will continue to run until the player chooses to quit.

During the game, the player can choose to hit or stand using the keyboard. The game will then determine the winner based on the highest score without going over 21.

Note
You can replace <<deck_id>> with "new" to create a shuffled deck and draw cards from that deck in the same request.

Enjoy playing Blackjack!
