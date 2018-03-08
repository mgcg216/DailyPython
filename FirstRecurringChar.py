
"""Write a program that outputs the first recurring character in a string."""
def main():
    inp = input("Enter you input: ")
    search(inp)

def search(inp):
    for i, char in enumerate(inp): #use enumerate more
        if char in inp[i+1:]: #very easy compare
            print(char)
            break
    else:
        print("No recurring char")

main()

