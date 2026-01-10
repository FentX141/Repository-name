# TODO Напишите функцию find_common_participants

def find_common_participants(group1,group2,razdelenie=","):
    sc1=set(group1.split(razdelenie))
    sc2=set(group2.split(razdelenie))
    common_participants = sc1.intersection(sc2)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group,razdelenie=",""|"))