import random
word_list = ["arecibo", "guaynabo", "caguas", "ponce", "hormigueros", "cayey", "loiza", "jayuya", "fajardo", "lares"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("A jugar hanged man")
    print("The theme is Puerto Rico Municipios")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
           if guess in guessed_letters:
              print("You already tried " + guess)
           elif guess not in word:
              print(guess + " isn't in the word :)")
              tries -= 1
              guessed_letters.append(guess)
           else:
              print("Nice one! "+ guess + " was in thex word!!!!")
              guessed_letters.append(guess)
              word_as_list = list(word_completion)
              indices = [i for i, letter in enumerate(word) if letter == guess]
              for index in indices:
                 word_as_list[index] = guess
              word_completion = "".join(word_as_list)
              if "-" not in word_completion:
                 guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
               print("you already tried " + guess + " !")
            elif guess != word:
               print(guess, "in't the word!")
               tries -= 1
               guessed_words.append(guess)
            else:
               guessed = True
               word_completion = word
        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
      print("FELICIDADES!! LO SACASTE BIEEEEEN")
    else:
      print("sorry bro you ran outta tries, the word was " + word)



def display_hangman(tries):
    stages = [ """
                  -------
                  |   |
                  |   O
                  |  /|\\
                  |  / \\
                  |
                  ---
               """,
               """
                  -------
                  |   |
                  |   O
                  |  /|\\
                  |  / 
                  |
                  ---
               """,
               """
                  -------
                  |   |
                  |   O
                  |  /|\\
                  |  
                  |
                  ---
               """,
               """
                  -------
                  |   |
                  |   O
                  |  /|
                  |  
                  |
                  ---
               """,
               """
                  -------
                  |   |
                  |   O
                  |   |
                  |  
                  |
                  ---
               """,
               """
                  -------
                  |   |
                  |   O
                  |  
                  |  
                  |
                  ---
               """,
               """
                  -------
                  |   
                  |   
                  |  
                  |  
                  |
                  ---
               """,
      ]
    return stages[tries]
def main():
   word = get_word(word_list)   
   play(word)
   while input("Again? (Y/N) ").upper() == "Y":
      word = get_word(word_list)
      play(word)
if __name__ == "__main__":
   main()
