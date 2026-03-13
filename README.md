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
hangman-game/    

├── hangmanGame.py         # Main program
└── README.md           # Project Documentation
``` 

# 6. Example Output

``` plaintext

* * * * * * Menu * * * * * *
----------------------------
1  Margherita          6.5       
2  Farm House          6         
3  Peppy Paneer        7.5       
4  Mexican Green Wave  7         
5  Deluxe Veggie       8         
6  Veg Extravaganza    8.5       
7  Cheese n Corn       5         
8  Fresh Veggie        5.5       
9  Veggie Paradise     6.5       
10 Special             9         
----------------------------
Would you like to place an order? yes/no: yes
Place your order, Pick a number to choose a pizza and after that type the quantity of that product.
If you like to stop, type -1
Press 0 to modify your order
Choose a number between 1 and 10: 1
Type the quantity of that product: 2
2  Margherita          13.0      
----------------------------
13.0
Choose a number between 1 and 10: 7
Type the quantity of that product: 1
2  Margherita          13.0      
1  Cheese n Corn       5         
----------------------------
18.0
Choose a number between 1 and 10: 0
2  Margherita          13.0      
1  Cheese n Corn       5         
----------------------------
18.0
Which row would you like to modify? 1
Type the new quantity: 1
1  Margherita          6.5       
1  Cheese n Corn       5         
----------------------------
11.5
Choose a number between 1 and 10: 0
1  Margherita          6.5       
1  Cheese n Corn       5         
----------------------------
11.5
Which row would you like to modify? 2
Type the new quantity: 0
1  Margherita          6.5       
----------------------------
6.5
Choose a number between 1 and 10: 10
Type the quantity of that product: 2
1  Margherita          6.5       
2  Special             18        
----------------------------
24.5
Choose a number between 1 and 10: -1
1  Margherita          6.5       
2  Special             18        
----------------------------
24.5
1  Margherita          6.5       
2  Special             18        
----------------------------
Checkout:              24.5

Process finished with exit code 0

```

# 7. Future Improvements
Some future improvements I keep in mind are:
* Keep track of orders using a database
* Make the program flexible by creating a non-stable menu
* Re-write the program using object-oriented programming
