import statistics

list_of_numbers = str(input("Enter numbers separated by spaces: ")).split()

new_list = []
for item in list_of_numbers:
    number = int(item)
    new_list.append(number)

print(new_list)
print("Mean:", statistics.mean(new_list))
print("Min:", min(new_list))
print("Max:", max(new_list))
print("Count:", len(new_list))