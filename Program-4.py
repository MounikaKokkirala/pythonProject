def no_of_multiplies(num_list, i):
    counter = 0

    for num in num_list:
        if (int(num) % i == 0):
            counter += 1

    return counter


num_list = list(input("Enter the integers seperated with comma: ").split(","))
dict_a = {}
for i in range(1, 10):
    count = no_of_multiplies(num_list, i)
    dict_a[i] = count
print(dict_a)