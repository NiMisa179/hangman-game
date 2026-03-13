# hangman-game
The well-known Hangman Game is implemented by this project. The project contains my first API call in Python.
The dictionary of the game is provided by API. When called, a random word is stored in the variable word. If there is an error with the API call, the error is printed and the variable word is empty.
The user has 8 guesses to reveal the word and win the game. For each wrong guess a body part is drawn, so the user knows how many tries they have. 
When the whole person is drawn and the word is not guessed yet, the number of guesses is 0 and the user have lost the game. If the game is lost, the word is revealed at the end.
For each right guess, the letter or the letters are written on the screen.
The user cannot type the same letter more than once, whenever this is a right or a wrong guess.
Have fun playing my Hangman Game!
