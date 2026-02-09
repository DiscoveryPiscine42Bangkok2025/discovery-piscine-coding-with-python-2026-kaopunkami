def main():
    try:
        n = int(input())
    except ValueError:

        return

    if n < 0:
        print("This number is negative.")
    elif n > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")

if __name__ == "__main__":
    main()