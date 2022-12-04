## Split the file on two newlines in a row
## Then add all the numbers together
## Then give the top input of combined

highestValue = 0

with open('day1-input.txt', 'r') as day1input:
    x = day1input.read().split("\n\n")

    for i in x:
        try:
            t = sum([int(x) for x in i.split("\n")])
            if t > highestValue:
                highestValue = t
        except:
            print()

print (highestValue)
