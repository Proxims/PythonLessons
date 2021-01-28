# Lessson 9 Lists Part 2

#index  0     1     2      3       4
cars=['bmv','vw','seat','skoda','lada']
for car in cars:
    print(car.upper())              # По-умолчанию вывод построчно. Одной строкой (print(car.upper(),end=' ')

print("------------------------\n")

for x in range(1,6):
    print(x)

print("------------------------\n")

mynumber_list=list(range(0,10))
print(mynumber_list)

print("------------------------\n")

for x in mynumber_list:
    x = x*2
    print(x)

print("------------------------\n")
print("Max number is: " + str(max(mynumber_list)))
print("Min number is: " + str(min(mynumber_list)))
print("Summa number is: " + str(sum(mynumber_list)))
print("------------------------\n")

#index -5     -4   -3     -2      -1          если считать с конца
#index  0     1     2      3       4
cars=['bmv','vw','seat','skoda','lada']

mycars=cars[1:4]                # С 1 значения списка до 4 (не включая 4)
print(mycars)
mycars=cars[:4]                 # С начала значения списка до 4 (не включая 4)
print(mycars)
mycars=cars[-3:-1]              # Отсчет с конца списка с -3 значения до -1 (не включая -1)
print(mycars)
print("------------------------\n")
#index  0     1     2      3       4
cars=['bmv','vw','seat','skoda','lada']
mycars = cars                   # Приравнивание списков, добавляя в 1 список добалвяется и в другой
cars.append('opel')
print(cars)
print(mycars)
print("------------------------\n")
#index  0     1     2      3       4
cars=['bmv','vw','seat','skoda','lada']

mycars = cars[:]                # Копирование всех значений списка cars в mycars без взаимосвязи списков
cars.append('opel')
print(cars)
print(mycars)