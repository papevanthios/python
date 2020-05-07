def my(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1] #Reverse the items of the list
    print(' '.join(reverse_word_list))
my("I am home")

