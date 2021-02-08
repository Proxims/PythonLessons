# Lessson-15-Functionss-part2

def create_record (name, telephone, city):
    """Create Recrods"""
    record = {
        'Name': name,
        'Tel': telephone,
        'City': city
     }
    return record


def give_award (medal, *persons):
    """Give Award"""
    for person in persons:
        print("Mr. " +person.title() + " nagrazhdaetsya medalyu " +medal)


user1 = create_record("Vasya","+9125002030","Moscow")
user2 = create_record("Petya","+9236003121","St.Petersburg")

print(user1)
print(user2)
print("--------------------------\n")

give_award("Za Berlin", "vasya", "petya")
