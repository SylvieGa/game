"""
Aufgabe 11.1: Add some more data in the dictionary
[X] Save number of attempts and the date
[X] Save the Players Name an the secret number in each game
Aufgabe 11.2: Add unsuccessful guesses into the dictionary
[X] Save the unsuccessful guesses
[X] Store the unsuccessful guesses in the dictionary ("wrong_guesses")
Aufgabe 11.3: Print out only the top 3 results
[X] Find a way to sort the scores ("score_lost.sort()" doesn`t work with dictionarys)
"""
import json
import random

filename = "score.json"

vonNum = 1
bisNum = 10


print("Welcome to 'Guess the Secret Number' But first...")

#Die unbekannte Zahl
secret = random.randint(vonNum, bisNum)

#Das Datum
from datetime import date
today = date.today()

#Die Spielernamen und das Raten der Nummer
player = input("Tell me your Player Name: ")

numGuess = 0

#falsche, geratene Nummer
wrongGuesses = 0

#Fragen nach dem Raten und der Gültigkeit der secret number
while True:
    try:
        UserGuess = int(input("Abracadabra, which number is in my mind? Tell me number between " + str(vonNum) + " and " + str(bisNum) + ": "))
        numGuess = numGuess + 1
        if UserGuess < vonNum or UserGuess > bisNum:
            raise ValueError
        elif int(UserGuess) == secret:
            print("You were right! That's the number.")
            break
        else:
            wrongGuesses = wrongGuesses + 1
            print("Sorry, no - that's not my number.")
    except ValueError:
        print("no valid number, sorry! Try again.")

listContent = {}
listContent['games'] = []

with open(filename) as json_file:
    listContent = json.load(json_file)

listContent['games'].append({
    "secretnumber": secret,
    "date": str(today),
    "player": player,
    "gTotal": numGuess,
    "gWrong": wrongGuesses
})

with open(filename, 'w') as f:
    json.dump(listContent, f)

sorted = sorted(listContent['games'], key = lambda i: i['gTotal'])

print("Top three Players: ")

countGames = 0

for game in sorted:
    countGames = countGames + 1
    print("#" + str(countGames) + " " + game["player"] + " with " + str(game["gTotal"]) + " attempts.")
    if countGames == 3:
        break