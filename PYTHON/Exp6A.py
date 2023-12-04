
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

with open("T1.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

with open("T1.txt", "r") as file:
    data = file.readlines()
    data = [int(num.strip()) for num in data]
    sorted_data = sorted(data)

with open("T2.txt", "w") as file:
    for num in sorted_data:
        file.write(str(num) + "\n")
