
start = '''
You and your bestfriend are going for a walk on the nature trail.
You've been walking for about 2min and you come across a huge muddy pothole.
You and your bestfriend decide to go on a detour. To avoid getting muddy,
you cut through a couple of bushes and come across a secret trail.
You can only go left or right. Which way do you decide to go?
'''

print(start)

while True: # only occurs if you type given options otherwise it asks question again
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        print("You decide to go left and find yourself in a dark forest.You hear a noise coming from the left but complete silence coming from the right. Which way do you go now?")
        if True: # only occurs if you type given options otherwise it asks question again
                print("Type 'left' to go left or 'right' to go right.")
                user_input = input()
                if user_input == "left":
                    print("You find a unknown creature eating the brains of a human. He senses you and your bestfriends presence. He slowly turns and starts to chase you. RUN!")
                    break # exits out of program
                elif user_input == "right":
                    print("You find a path out of the forest and ironically you end up right in front of your home. Safe and sound.")
                    break # exits out of program
                else: print("Try again!")

    elif user_input == "right":
        print("You choose to go right and find yourself at a park. You don't hear anything coming from either side. Your bestfriend mumbles something about wanting to get out of here. So you decide your direction off of instinct. Which direction do you go?")
        if True: # only occurs if you type given options otherwise it asks question again
                print("Type 'left' to go left or 'right' to go right")
                user_input = input()
                if user_input == "left":
                    print("You successfully found your way back!")
                    break # exits out of program
                elif user_input == "right":
                    print("You're back at where you started.")
                    print(start) # goes back to beginning and starts over
                else: print("Try again!")

    else: print("Try again!")
