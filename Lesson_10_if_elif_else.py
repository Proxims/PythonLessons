# Lesson-10-Условне операторы if-elif-else

age = 14

if (age <=4):
    print("You are baby")
elif (age >4) and (age <12):
    print("You are kid")
elif (age >=12) and (age <19):
    print("You are teenager")
else:
    print("You are adult")

print("-------END---------\n")

all_cars = ['chrusler', 'dacia', 'bmv', 'KIA', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'chevrolett']
german_cars = ['bmv', 'vw', 'audi']

for car in all_cars:
    if car in german_cars:
        print(car + " " + "In german list")
    else:                                      # Если убрать эти 2 строки то будут печататься только совпадения
       print(car + " " + "Is not german car")  #




