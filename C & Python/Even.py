
numb = [1, 3, 7, 9, 12, 5, 8]

i = 0
while i < len(numb):
    if numb[i] % 2 == 0:
        print("First even number found:", numb[i])
    i = i + 1
else:
    print("No more even numbers found")