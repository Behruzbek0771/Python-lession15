words = ["kitob", "dastur", "AI", "hello", "python", "fdsf", "fdsafadsfds"]

group_of_words = [
    [],  # 0 - qisqa so‘zlar (<=3 harf)
    [],  # 1 - o‘rta so‘zlar (4-6 harf)
    []   # 2 - uzun so‘zlar (>6 harf)
]

for word in words:
    if len(word) <= 3:
        group_of_words[0].append(word)
    elif len(word) <= 6:
        group_of_words[1].append(word)
    else:
        group_of_words[2].append(word)

print(group_of_words)
