def ac(text):
    wordlist = text.lower().split()
    print(wordlist[0][0] == wordlist[1][0])
ac('hello hi')
ac('hello ai')