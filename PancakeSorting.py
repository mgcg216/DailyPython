"""I work as a waiter at a local breakfast establishment. The chef at the pancake house is sloppier than I like, and
when I deliver the pancakes I want them to be sorted biggest on bottom and smallest on top. Problem is, all I have is a
spatula. I can grab substacks of pancakes and flip them over to sort them, but I can't otherwise move them from the
middle to the top.

How can I achieve this efficiently?

This is a well known problem called the pancake sorting problem. Bill Gates once wrote a paper on this that established the best known upper bound for 30 years.

This particular challenge is two-fold: implement the algorithm, and challenge one another for efficiency."""

"""After read up here http://datagenetics.com/blog/february42018/index.html
i think i have a good algorithm
Find the largest pancake and flip it to the top then flip the whole stack to put it on the bottom repeat as if the largest
pancake doesnt exist etc"""

num_of_pan = 8
pan_ord = [7, 6, 4, 2, 6, 7, 8, 7]



def panSort(num_of_pan,pan_ord):
    fin_ord = []
    num_of_flips = 0
    pos = 0

    while len(fin_ord) != num_of_pan:
        #if max(pan_ord) == pan_ord[0]:
        for i, c in enumerate(pan_ord): #checks where the largest pancake position
            print(i,c)
            if c == max(pan_ord):
                pos = i
        #now that i have the position i need to flip
        tmp = pan_ord[pos:]
        pan_ord = pan_ord[:pos] +tmp[::-1]
        pan_ord = pan_ord[::-1]
        print(pan_ord)
        fin_ord = fin_ord + pan_ord[:1]
        print(pan_ord)
        pan_ord = pan_ord[1:]
        num_of_flips = num_of_flips + 1


    return fin_ord, num_of_flips
def main():
    fin_ord, num_of_flips = panSort(num_of_pan, pan_ord)
    print(fin_ord, num_of_flips)

main()