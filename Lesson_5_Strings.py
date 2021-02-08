# Lesson 5 Strings

mystring = "Bla Bla"

name ="mIkhAil lantSov"

print(name)
print(name.title())
print(name.upper())
print(name.lower())
print("------------------------\n")
print("Stroka 1\nStroka 2\n\nStroka 3")
print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEND")
print("Lower name: " + name.lower())
print("------------------------\n")
a= "          / . + dyadya vasya . . -    "
print(a)
print(a.rstrip())                   # Удалить пробелы справа
print(a.lstrip())                   # Удалить пробелы слева
print(a.strip())                    # Удалить пробелы с двух сторон
print(a.strip(". + - /"))           # Удалить с двух сторон пробелы . + - /
