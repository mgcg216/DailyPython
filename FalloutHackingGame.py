"""The popular video games Fallout 3 and Fallout: New Vegas have a computer "hacking" minigame where the player must correctly guess the correct password from a list of same-length words. Your challenge is to implement this game yourself.

The game operates similarly to the classic board game Mastermind. The player has only 4 guesses and on each incorrect guess the computer will indicate how many letter positions are correct.

For example, if the password is MIND and the player guesses MEND, the game will indicate that 3 out of 4 positions are correct (M_ND). If the password is COMPUTE and the player guesses PLAYFUL, the game will report 0/7. While some of the letters match, they're in the wrong position.

Ask the player for a difficulty (very easy, easy, average, hard, very hard), then present the player with 5 to 15 words of the same length. The length can be 4 to 15 letters. More words and letters make for a harder puzzle. The player then has 4 guesses, and on each incorrect guess indicate the number of correct positions."""


"""Maybe sloppy code but it works"""
import random

def main():
    print("Lets play")
    print("1. Very Easy 2. Easy 3. Average 4. Hard 5. Very Hard")
    dif = input("Choose Difficulty:")
    min, max = difficulty(int(dif))
    answer, wordlist, wordsize = ReadFile(int(min),int(max))
    guess = 4
    while guess != 0:
        print(wordlist)
        inp = input(":")
        Choose(answer, wordlist, wordsize, inp)
        if guess == 0:
            print("You Lose")

def difficulty(dif):
    #min, max = 0
    if dif == 1: #very easy
        min = 4
        max = 6
    elif dif ==2: #easy
        min = 7
        max = 8
    elif dif ==2: #average
        min = 9
        max = 11
    elif dif ==2: #hard
        min = 12
        max = 13
    elif dif ==2: #very hard
        min = 14
        max = 15
    else:
        print("err")
        exit()
    return min, max

def ReadFile(min, max):
    wordsize = random.randint(min,max)
    print(wordsize)
    in_file = open("enable1.txt","r")
    contents = in_file.read().splitlines()
    in_file.close()
    result = []
    for content in contents:
        if len(content) == wordsize:
            result.append(content)
    wordlist=[]
    for x in range(0,int(max)):
        wordlist.append(random.choice(result))
    answer = random.choice(wordlist)
    return answer, wordlist, wordsize

def Choose(answer, wordlist, wordsize, guess):
    print(answer)
    print(wordlist)
    num_cor = 0
    for c, letter in enumerate(answer,0):
        #print(c, letter, guess[c])
        if ord(letter) == ord(guess[c]):
            num_cor = num_cor + 1
    print(num_cor, "/", wordsize)
    if num_cor == wordsize:
        print("You Win")
        exit()
"""
answer = "transuranium"
wordlist = ['idolatrously', 'diversifiers', 'transuranium', 'dialectology', 'redirections', 'punitiveness', 'nonarguments', 'unrepeatable', 'rattlebrains', 'irredentists']
guess =  "transuranaaa"
"""

main()