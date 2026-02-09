def main():
    prompt = "What you gotta say? : "
    msg = input(prompt)

    while msg != "STOP":
        prompt = "I got that! Anything else? : "
        msg = input(prompt)

if __name__ == "__main__":
    main()