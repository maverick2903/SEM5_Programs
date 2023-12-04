with open('T1.txt', 'r') as file:
    contents = file.read()

words = contents.split()

sorted_words = sorted(words)

with open('T2.txt', 'w') as file:
    file.write('\n'.join(sorted_words))
