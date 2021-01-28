# Lesson 6 Loops


print("*****")
print("*****")
print("*****")
print("*****")
print("*****")
print("----------END OF BLOCK-------------\n")

for x in range(0,100,2):                   # В диапазоне цифры означают (Начальное число, конечное число, щаг)
    print("* Nomer x= " +str(x) +" *")

print("----------END OF BLOCK-------------\n")

while True:
    print(x)
    x=x+1
    if x==100:
        break