# Lesson-11-Dictionary Part 2



#         #######Item#######
#         #KEY#      #VALUE#

enemy = {
         'loc_x':      70,
         'loc_y':      50,
         'color':     'green',
         'health':     100,
         'name':      'Monster',
         'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

all_enemies=[]

for x in range (0, 10):
    all_enemies.append(enemy.copy())
for en in all_enemies:
    if en['health'] <= 80 and en['health'] > 50:
        en['color'] = 'yellow'
    elif en['health'] <= 50 and en['health'] > 30:
        en['color'] = 'red'
    elif en['health'] <= 30 and en['health'] > 0:
        en['color'] = 'dark red'
    elif en['health'] == 0:
        en['color'] = 'black'
    print(en)

all_enemies[5]['health'] = 60
all_enemies[8]['health'] = 30
all_enemies[2]['name'] = 'Beastmen'

for en in all_enemies:
    if en['health'] <= 80 and en['health'] > 50:
        en['color'] = 'yellow'
    elif en['health'] <= 50 and en['health'] > 30:
        en['color'] = 'red'
    elif en['health'] <= 30 and en['health'] > 0:
        en['color'] = 'dark red'
    elif en['health'] == 0:
        en['color'] = 'black'
    print(en)

