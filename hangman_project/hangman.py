import requests

symbol = 'AAPL'
url = "https://api.api-ninjas.com/v2/randomword?ticker={}".format(symbol)

response = requests.get(url, headers={'X-Api-Key':'YOUR-API-KEY'})
if response.status_code == 200:
    data = response.json()
    # print(data[0])
    word = data[0]
else:
    word = ""
    print(response.status_code)

print("Welcome to Hangman game!")
print("A random word has picked")
print("You guess the word, you WIN!!")
print("You have 8 guesses. For each wrong guess a body part will be drawn")
print("When the little person appears it means you have lost the game")

hidden = ["-" for i in word]
word_list = [i for i in word]
let_guesses = []


guesses = 8
cont = True

while guesses > 0 and cont:

    for i in hidden:
        print(i, end=" ")
    print()

    letter = input("Enter your guess: ")
    while letter in let_guesses:
        print("You have already picked", letter, ". Please pick another letter.")
        letter = input("Enter your guess: ")
    let_guesses.append(letter)

    if letter in word:
        count = -1
        for i in word:
            count = count + 1
            if i == letter:
                hidden[count] = letter
    else:
        print("Wrong guess. The chosen word has not any", letter)
        print("  O ")
        if guesses == 7:
            print("-")
        elif guesses == 6:
            print("--")
        elif guesses == 5:
            print("--|")
        elif guesses == 4:
            print("--|-")
        elif guesses == 3:
            print("--|--")
        elif guesses == 2:
            print("--|--")
            print(" /")
        elif guesses == 1:
            print("--|--")
            print(" / \\")
        guesses -= 1

    if "-" not in hidden:
        cont = False

if not cont:
    for i in hidden:
        print(i, end=" ")
    print()
    print("You won! You guessed the word", word)
else:
    print("You lost :(. The word was", word)
