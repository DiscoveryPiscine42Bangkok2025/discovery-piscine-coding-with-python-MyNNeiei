def greetings(name):
    if name == None or name == "":
        print("Hello, noble stranger.\n")
    if isinstance(name, int):
        print("Error! It was not a name.\n")
    else:
        print("Hello", name + ".\n")
greetings('Alexzander')
greetings('Wil')
greetings()
greetings(42)