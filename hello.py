# prints Hello World
print("Hello World!")
answer = input("Who inspires you?")
print(answer, "inspires you!")

variable1 = 10
varibale2 = 30
boo1 = True
boo2 = False
string1 = "Strings"

print ("variable1 =", variable1)
print ("varibale2 =", varibale2)
print ("Added =", variable1 + varibale2)

ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
total = ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]
average = total/len(ages)
print(average)

ages = [5,12,3,56,24,78,1,15,44]
total = 0
for x in ages:
        total += x
        average = total / len(ages)
        print(average)

bob = "Georgia"
sue = 19
mary = True

word = "Georgia"

underscore = "_"
len(word) # length of the word is 7
print (len(word))
guessingword = []

# Goal = _ _ _ _ _ _ _
for x in word:
    guessingword.append("_");
    print (underscore)
