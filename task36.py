words = ["kitob", "dastur", "AI", "hello", "python"]

max_word = words[0]

for word in words[1:]:
    if len(word) > len(max_word):
        max_word = word

print(max_word)
