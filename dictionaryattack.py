#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
readMe = f.read()
f.close()

while True
    print("Can your password survive a dictionary attack?")

    test_password = input("Type in a trial password: ").lower()

    if test_password in readMe:
        print ("Your password is too weak. Try again.")
    else:
        print ("Awesome! Your password isn't in the dictionary.")
