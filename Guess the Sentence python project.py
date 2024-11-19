import random

def guess_the_sentence():
    print("Welcome to 'Guess the Sentence'!")
    
    sentences = [
        "Python is fun",
        "I love programming",
        "Let's play a game",
        "Coding is awesome",
        "Keep learning new things"
    ]
    

    secret_sentence = random.choice(sentences)

    scrambled_sentence = ''.join(random.sample(secret_sentence, len(secret_sentence)))
    
    print("\nThe scrambled sentence is:")
    print(scrambled_sentence)
    
  
    attempts = 0
    while True:
       
        guess = input("\nGuess the sentence: ").strip()
        attempts += 1
        
     
        if guess.lower() == secret_sentence.lower():
            print(f"\nCongratulations! You guessed the correct sentence in {attempts} attempts.")
            break
        else:
            print("Oops! Try again.")


guess_the_sentence()