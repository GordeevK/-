text = [s.lower() for s in input().split("-")]
count = (len(text))
for a in text:
    a.split()
    for b in a:
        if b in "wasd":
            count -= 1
            break
print(count)

