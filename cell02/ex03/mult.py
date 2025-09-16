def main():
    num1 = int(input("Enter the first number: \n"))
    num2 = int(input("Enter the second number: \n"))
    num_result = num1 * num2
    print(num1, "x", num2, "=", num_result)
    if(num_result < 0):
        print("The result is negative")
    elif(num_result > 0):
        print("The result is positive")
    else:
        print("The result is positive and negative")
main()