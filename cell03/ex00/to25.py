def main():
    print("Enter a number less than 25")
    s = input()

    try:
        n = int(s)
    except ValueError:
        print("Error")
        return

    if n > 25:
        print("Error")
        return

    while n <= 25:
        print(f"Inside the loop, my variable is {n}")
        n += 1

if __name__ == "__main__":
    main()