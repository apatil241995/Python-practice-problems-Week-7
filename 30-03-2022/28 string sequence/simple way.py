input_str = input("Enter the string: ")

list_ = input_str.split(',')

sorted_list = sorted(list_)

print(sorted_list)

sorted_str = ",".join(sorted_list)

print(sorted_str)