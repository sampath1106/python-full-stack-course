# Original list
input_list = [5, 6, 7, 8, 9]

# Store the last element in a temporary variable
last = input_list[-1]

# Shift all elements to the right by one position
for i in range(len(input_list) - 1, 0, -1):
    input_list[i] = input_list[i - 1]

# Put the last element at the first position
input_list[0] = last

print(input_list)
