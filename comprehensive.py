string = "hi hello Prabhas"
def vowel(string):
    vowels = [ch for ch in string if ch.lower() in "aeiou"]
    consonants = [ch for ch in string if ch.isalpha() and ch.lower() not in "aeiou"]
    print(vowels)
    print(consonants)
vowel(string)