def main():
    age = int(input("Please tell me your age: "))
    print("You are current", age, "years old.")
    for i in range(10, 40, 10):
        print("In", i, "years, you'll be", age + i, "years old.")
main()