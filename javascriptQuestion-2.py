# Question - 2 - Returns number of vowels

def numVowels(string):
    vowel = set("aeiouAEIOU")
    count = 0
    for i in string:
        if i in vowel:
            count += 1
    return count

numVowels("Hello World!")