def main():
    print("Enter a number")
    s = input()

    try:
        n = int(s)
    except ValueError:
 
        return

    i = 0
    while i <= 9:
        print(f"{i} x {n} = {i * n}")
        i += 1

if __name__ == "__main__":
    main()