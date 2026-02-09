def main():
    print("Enter the first number:")
    a = int(input())
    print("Enter the second number:")
    b = int(input())

    result = a * b
    print(f"{a} x {b} = {result}")

    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")

if __name__ == "__main__":
    main()