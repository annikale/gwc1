# --- Define your functions below! ---

def intro():
    print("Hi! My name is Bob.")


# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        answer = answer.lower()
        # print("That's cool!")
        process_input(answer)

def process_input(solution):
    greetings = ["hi", "hello", "what's up"]
    farewells = ["bye", "goodbye"]

    # if solution == "hi":
    if is_valid_input(solution, greetings):
        say_greeting()
    else:
        say_default()

    if is_valid_input(solution, farewells):
        say_goodbye()
    else:
        say_default()

def is_valid_input(user_input, valid_responses):
    for item in valid_responses:
        if user_input == item:
            return True
    return False

def say_greeting():
    print("Hey there!")

def say_default():
    print("That's cool!")

def say_goodbye():
    print("bye")
    exit()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
