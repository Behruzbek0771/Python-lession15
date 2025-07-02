royhat = [1, 2, 3, 4, 5, 6, 7, 8 ]
index = int(input(f"index kriting ( 0 - {len(royhat)-1}):"))
if 0<= index <= len(royhat):
    a = int(input("son kriting: "))
    royhat[index] = a
else:
    print(" siz xota index krittiz")

print(royhat)