def pd(text):
    result = ''

    for char in text:
        result += char*3
    print(result)

pd("Hello")
pd("Mississippi")