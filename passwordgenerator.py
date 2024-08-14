import random

letters = int(input("how many letters you want in your password ?"))

symbols = int(input("how many symbols you want in your password?"))

numbers = int(input("how many numbers you want in your password"))

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list2 = ['1','2','3','4','5','6','7','8','9','0']

list3 = ['!','@','#','$','%','^','&','*','~','`','/','?']

password_list =[]

for i in range(letters):
    
    
    password_list.append(random.choice(list1))

for i in range(symbols):

    password_list.append(random.choice(list2))

for i in range(numbers):
    
    password_list.append(random.choice(list3))

random.shuffle(password_list)
# print(password_list)

password = ""

print(password.join(password_list))

# for i in password:
#     new += i

# print(new)
