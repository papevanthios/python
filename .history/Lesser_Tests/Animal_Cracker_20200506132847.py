def ac(text):
    wordlist = text.split()

    first = wordlist[0]
    second = wordlist[1]

    print(first[0] == second[0])

ac('hello hi')