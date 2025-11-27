import random
l= len
def hangman():
    word_list = ["python", "hangman", "game", "song", "movies","winner","looser"]
    word = random.choice(word_list).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 3
    word_completion = "_" * l(word)
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses and "_" in word_completion:
        print("\nWord: " + " ".join(word_completion))
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Incorrect Guesses Left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if l(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
            word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
            
    if "_" not in word_completion:
        print(f"Congratulations! You guessed right: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()