# Lesson 8 Lists (Array) part 1

cities = ['New York', 'Moscow', 'sherbinka', 'Podolsk', 'St.Petersburg']
print(cities)
print(len(cities))
print(cities[1])
print(cities[-4])
print(cities[2].title())
print("------------------------\n")

cities[3] = 'Tula'
print(cities)
cities.append('Kursk')
cities.insert(2, 'Yalta')
print(cities)
print("------------------------\n")

del cities[3]
print(cities)
cities.remove('Tula')
print(cities)

deleted_city=cities.pop()
print("Deleted city is " + deleted_city)
cities.reverse()
print(cities)

