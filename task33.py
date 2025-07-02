list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
list_all = list1 + list2

result = []

for x in list_all:
    if list_all.count(x) > 1 and x not in result:
        result.append(x)
print(result)

    