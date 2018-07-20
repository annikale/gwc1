import json

# Creates the dictionary to store responses.
answers = {}

'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''
#make a list of questions
questions = [
    "What's your name?",
    "How old are you?",
    "favorite food?",
    "favorite color?",
    "birth month?"]

# make a list of keys
keys = [
    "name","age","food","color","month"]

# make a list of answers
listAnswers = []

#done = "no"

# make a loop to go through questions
while True:
    for x in range(len(questions)):
        response = input(questions[x] + " ")
        answers[keys[x]] = response

    listAnswers.append(answers)

#    done = input("Are you the last person?" "Yes or No?").lower()
# Print the context of the dictionary.
    print(listAnswers)
    print("are you the last person?")
    user_input = input()
    if user_input == "yes":
            break

#json= json.dumps(listAnswers)
#f = open("survey.json","w")
#f.write(json)
#f.close()

# json= json.dumps(listAnswers)
# f = open("survey.json","r")
# olddata = json.load()
# f.write(json)
#f.close()

f = open("survey.json", "a")
f.write('[\n')
index = 0
for t in listAnswers:
    if (index < len(listAnswers)-1):
        f.write(',\n')
    else:
        json.dump(t,f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
