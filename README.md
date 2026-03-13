# 1. Description
## hangman game
The well-known Hangman Game is implemented by this project. The dictionary of the game is provided by API.

# 2. Features
* A random word is stored in the variable word using an API call
* Uses Python Lists
* Displays the current state of the game. Once the player guesses a letter contained in the hidden word, it is revealed permanently
* For each wrong answer a body part is drawn

# 3. Technologies
* Python3
* Lists
* List processing
* Loops

# 4. Execute the program
1. Save the script as:
   hangmanGame.py
2. Run the program:
   python hangmanGame.py

# 5. Structure
``` text
hangman_progect/    

├── hangman.py         # Main program
└── README.md           # Project Documentation
``` 

# 6. Example Output

``` plaintext

Welcome to Hangman game!
A random word has picked
You guess the word, you WIN!!
You have 8 guesses. For each wrong guess a body part will be drawn
When the little person appears it means you have lost the game
- - - - - 
Enter your guess: f
- - - - f 
Enter your guess: a
Wrong guess. The chosen word has not any a
  O 
- - - - f 
Enter your guess: e
Wrong guess. The chosen word has not any e
  O 
-
- - - - f 
Enter your guess: r
- r - - f 
Enter your guess: f
You have already picked f . Please pick another letter.
Enter your guess: p
p r - - f 
Enter your guess: e
You have already picked e . Please pick another letter.
Enter your guess: d
Wrong guess. The chosen word has not any d
  O 
--
p r - - f 
Enter your guess: o
p r o o f 
You won! You guessed the word proof

Process finished with exit code 0

```
Failure
``` plaintext
Welcome to Hangman game!
A random word has picked
You guess the word, you WIN!!
You have 8 guesses. For each wrong guess a body part will be drawn
When the little person appears it means you have lost the game
- - - - - - - - - - - - 
Enter your guess: g
Wrong guess. The chosen word has not any g
  O 
- - - - - - - - - - - - 
Enter your guess: h
Wrong guess. The chosen word has not any h
  O 
-
- - - - - - - - - - - - 
Enter your guess: f
Wrong guess. The chosen word has not any f
  O 
--
- - - - - - - - - - - - 
Enter your guess: d
Wrong guess. The chosen word has not any d
  O 
--|
- - - - - - - - - - - - 
Enter your guess: b
Wrong guess. The chosen word has not any b
  O 
--|-
- - - - - - - - - - - - 
Enter your guess: g
You have already picked g . Please pick another letter.
Enter your guess: o
- - - o - - - - - - - - 
Enter your guess: e
e - - o - - - - - - - e 
Enter your guess: i
e - - o - - - - - i - e 
Enter your guess: n
Wrong guess. The chosen word has not any n
  O 
--|--
e - - o - - - - - i - e 
Enter your guess: b
You have already picked b . Please pick another letter.
Enter your guess: u
Wrong guess. The chosen word has not any u
  O 
--|--
 /
e - - o - - - - - i - e 
Enter your guess: p
e - - o p - - - - i - e 
Enter your guess: f
You have already picked f . Please pick another letter.
Enter your guess: t
e - t o p - - - - i t e 
Enter your guess: m
Wrong guess. The chosen word has not any m
  O 
--|--
 / \
You lost :(. The word was ectoparasite

Process finished with exit code 0

```

# 7. Future Improvements
* GUI

# 8. Author
Nikos Misailidis
Github: https://github.com/NiMisa179
