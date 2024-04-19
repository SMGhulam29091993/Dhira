
def numVowels(string):
    vowel = set("aeiouAEIOU")
    count = 0
    newWord = ""
    for i in string:
        if i in vowel:
            count += 1
            newWord += i.upper()
        else:
            newWord += i
    return count

print(numVowels("Hello World!"))
