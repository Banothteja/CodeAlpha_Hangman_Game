import random

# Categories and Corresponding word lists
categories = {
    'bike': ['kawasaki', 'ducati', 'suzuki', 'ktm', 'triumph'],
    'car': ['supra', 'hatchback', 'bmw', 'lamborghini', 'jaguar'],
    'sports': ['basketball', 'football', 'tennis', 'volleyball', 'badminton']
}

# ASCII art representation of the hangman
hangman_stages = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    '''
]

# Function to choose a category and word from that category
def choose_category():
    print("Choose a category:")
    for idx, category in enumerate(categories.keys()):
        print(f"{idx + 1}. {category.capitalize()}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            category = list(categories.keys())[choice - 1]
            word = random.choice(categories[category])
            return category, word
        except (IndexError, ValueError):
            print("Invalid input. Please enter the number of the category you want to play.")

# Function to display the current state of the word with gussed letters
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game function
def play_hangman():
    print("Welcome to Hangman!\n")
    player_name = input("Enter your name: ")
    category, word = choose_category()

    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print(f"\nWelcome, {player_name}! Let's play Hangman in the category: {category.capitalize()}")
    print("You have to guess the word letter by letter.")
    print(f"You are allowed {max_incorrect_guesses} incorrect guesses.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word:", display_word(word, guessed_letters))
        print("\n" + hangman_stages[incorrect_guesses])

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)
        print("\n" + hangman_stages[incorrect_guesses])

# Run the game
if __name__ == "__main__":
    play_hangman()
