phrase = input("Enter a phrase: ")

def wordCount(phrase):
    words = phrase.split()
    return len(words)

print("Number of words: ", wordCount(phrase))