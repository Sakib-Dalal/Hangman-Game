
import random

word_list = ["aardvark", "baboon", "camel"]
chose = random.choice(word_list)

guess = input("Guess a letter: ")

for i in range(len(chose)):
    if guess == chose[i]:
        print("Right")
    else:
        print("Wrong")
