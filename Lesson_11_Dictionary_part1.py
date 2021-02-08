# Lesson-11-Dictionary Part 1


#         #######Item#######
#         #KEY#      #VALUE#

enemy = {
         'loc_x':      70,
         'loc_y':      50,
         'color':     'green',
         'health':     100,
         'name':      'Monster',
}
print("Location x = " +str(enemy['loc_x']))
print("Location y = " +str(enemy['loc_y']))
print("Name: " + (enemy['name']))

enemy['rank'] = 'Gold'
print(enemy)

del enemy['rank']

print(enemy)

enemy['loc_x'] +=40                                     # Изменение параметров словаря
enemy['health'] -=20
if enemy['health'] <= 80 and enemy['health'] >50:
    enemy['color'] = 'yellow'
elif enemy['health'] <= 50 and enemy['health'] >30:
    enemy['color'] = 'red'
elif enemy['health'] <= 30 and enemy['health'] >0:
    enemy['color'] = 'dark red'
elif enemy['health'] == 0:
    enemy['color'] = 'black'

print(enemy)


print(enemy.keys())
print(enemy.values())