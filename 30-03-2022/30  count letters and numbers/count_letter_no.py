sentence = input("Enter the sentence: ")
letter_count = 0
uppercase_count = 0
lowercase_count = 0
digits_count = 0

for i  in sentence:
  if i.isnumeric():
    digits_count += 1
  
  if i.isalpha():
    letter_count += 1
    if i.isupper():
      uppercase_count += 1
    elif i.islower():
      lowercase_count += 1

print("digits count: ",digits_count)
print("letter count: ", letter_count)
print("uppercase letters count: ",uppercase_count)
print("lowercase letters count: ",lowercase_count)