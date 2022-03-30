def password_check(password):
  count = 0
  lis = ['@','$','#']

  if 7<= len(password) <=12:
    for i in password:
      if i.isalpha():
        count += 1
        break
    
    for j in password:
      if j.isupper():
        count += 1
        break

    for k in password:
      if k.isnumeric():
        count += 1
        break
    
    for l in password:
      if l in lis:
        count += 1
        break
    
    if count == 4:
      return f"password accepted {password}"
    
    else:
      return "password not accepted"
    

  else:
    return "Password is too small or too big"

if __name__ == "__main__":
  password = input("Enter password: ")
  print(password_check(password))