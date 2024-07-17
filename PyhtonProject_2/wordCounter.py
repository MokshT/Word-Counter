sentence = input("Enter a sentence: ").replace(',', '').lower().split()
wc = {}

for word in sentence:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1

print(wc)
