"""Disemvoweling means removing the vowels from text. (For this challenge, the letters a, e, i, o, and u are considered vowels, and the letter y is not.)
The idea is to make text difficult but not impossible to read, for when somebody posts something so idiotic you want people who are reading it to get extra frustrated."""

inp = "two drums and a cymbal fall off a cliff"
delthis = ["a","e","i","o","u"," "]
print("".join(letter for letter in inp if letter in delthis)) #reddits way interesting way to join vowels
for x in delthis: #my way not as cool to remove vowels
    inp = inp.replace(x,"")
print(inp)