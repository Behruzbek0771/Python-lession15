words = []
for i in range(5):
    word =input(f"{i+1} - so'z kriting: ")
    words.append(word)
    
palindrom_words = []
for word in words:
    if word == word[::-1]:
        palindrom_words.append(word)

print(palindrom_words)

