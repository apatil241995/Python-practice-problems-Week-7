nested_list = [1,2,3,4,[5,6,7,8],9,10,[20,11,12]]

sub_list = ["i","am","sub list"]

index = int(input("enter the index: "))

nested_list.insert(index,sub_list)

print(nested_list)