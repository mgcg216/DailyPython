"""Short links have been all the rage for several years now, spurred in part by Twitter's character limits.
 Imgur - Reddit's go-to image hosting site - uses a similar style for their links.
 Monotonically increasing IDs represented in Base62.
Your task today is to convert a number to its Base62 representation."""

Base64 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
    inp = input("What is the Input: ")
    print(convert(int(inp)))

def convert(inp):
    con = ""
    while(inp>64):
        con = Base64[int(inp%64)] + con
        inp=inp/64
    con = Base64[int(inp % 64)] + con

    return con


main()