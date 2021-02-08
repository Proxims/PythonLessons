# Lesson-13-Input

name = input("Please enter ypur name: ")

print("Privet " +name)

print("------------------------\n")

num1 = input("Enter X: ")
num2 = input("Enter Y: ")
                                # По умолчанию Input вводит строчные значения,
summa = int(num1) + int(num2)   # конвертируем в цифровые при помощи int()
print(summa)

print("------------------------\n")

message =""
while message != 'sekret':
    message = input("Enter password ")
    print(message + " Wrong password")
else:
    print(message + " Correct password")

print("------------------------\n")

mylist = []
msg= ""
while msg.upper() != 'STOP':
        msg = input("Enter new item, and STOP to finish: ")
        if msg.upper() == 'STOP':
            break
        else:
            mylist.append(msg)
print(mylist)