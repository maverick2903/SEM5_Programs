with open("T1.txt", "r") as input_file:
    words = input_file.read().split()

reversed_words = []

for word in words:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)

reversed_words.sort()

with open("T2.txt", "w") as output_file:
    for reversed_word in reversed_words:
        output_file.write(reversed_word + "\n")
