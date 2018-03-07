def main():
    """"Hangman game"""
    inp = input("What is the word or sentence?")
    empty = tran(splitter(inp))
    code = splitter(inp)
    guess(code, empty)

def splitter(inp):
    #a = "Hello world!"
    listresp = list(map(list, inp))
    listff = []
    for charersp in listresp:
        for charfinnal in charersp:
            listff.append(charfinnal)
    return listff

def tran(ar):
    emp = []
    for x in ar:
        if (ord(x) >= 97 and ord(x) <= 122):
            emp.append("-")
        else:
            emp.append(" ")
    return emp

def guess(code, empty):
    tries = 10
    correct = 0
    while tries != 0:
        print(empty)
        print("You have ", tries, " many tries")
        inp = input("Enter Letter: ")
        i = 0
        while i < len(code):
            if(ord(code[i]) == ord(inp)):
                empty[i]=inp
                correct = 1
            i = i + 1

        if(correct == 0):
            tries = tries - 1
        correct = 0








main()
