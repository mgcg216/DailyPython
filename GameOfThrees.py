"""Back in middle school, I had a peculiar way of dealing with super boring classes. I would take my handy pocket calculator and play a "Game of Threes". Here's how you play it:

First, you mash in a random large number to start with. Then, repeatedly do the following:

If the number is divisible by 3, divide it by 3.
If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
The game stops when you reach "1".

While the game was originally a race against myself in order to hone quick math reflexes, it also poses an opportunity for some interesting programming challenges. Today, the challenge is to create a program that "plays" the Game of Threes."""

def main():
    inp = input("What is the input: ")
    threes(int(inp))

def threes(x):
    while x != 1:
        print(x)
        if x%3 == 0:
            x = x/3
        elif x%3 == 1:
            x = x - 1;
        elif x%3 == 2:
            x = x + 1
        else:
            print("I am error")
    print(x)

main()