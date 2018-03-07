"""Rabbits are known for their fast breeding, but how soon will they dominate the earth?

Starting with a small population of male and female rabbits we have to figure out how long it will take for them to outnumber humans 2:1.

Every month a fertile female will have 14 offspring (5 males and 9 females).

A female rabbit is fertile when it has reached the age of 4 months, they never stop being fertile.

Rabbits die at the age of 8 years (96 months)."""

def main():
    death_age = 96
    init_age = 2
    rabbit_male, rabbit_female = [[0 for x in range(death_age)] for i in range(2)] #interesting to populate an array
    init_m = input("Please Enter the Number of Male Rabbits: ")
    init_f = input("Please Enter the Number of Female Rabbits: ")
    human = input("Please Enter the Number of Humans: ")

    rabbit_male[init_age], rabbit_female[init_age] = int(init_m), int(init_f)
    month = 0
    while sum(rabbit_male) + sum(rabbit_female) < int(human):
        baby = sum(rabbit_female[4:])
        rabbit_female = [9 * baby] + rabbit_female[:-1]
        rabbit_male = [5 * baby] + rabbit_male[:-1]
        month = month + 1
    print(month)


    
main()
