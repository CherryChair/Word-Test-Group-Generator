import random


def input_numbers():
    people_number = int(input("Ile jest osób w klasie: "))
    groups_number = int(input("Ile jest grup: "))
    tasks_number = int(input("Ile jest zadań: "))
    group_task_divison = input("Jaki jest podział przydzielonych zadań z grupy: ").split()
    info_table = []
    info_table.append(people_number)
    info_table.append(groups_number)
    info_table.append(tasks_number)
    new_table = []
    for item in group_task_divison:
        new_table.append(int(item))
    if sum(new_table) + groups_number != people_number:
        print("Zły podział przydzielonych zadań z grupy.")
        exit()
    info_table.append(new_table)
    return info_table


def create_task_division(info_table):
    people_number = info_table[0]
    groups_number = info_table[1]
    tasks_number = info_table[2]
    group_task_divison = info_table[3]

    task_dict = {}

    for i in range(1, people_number + 1):
        task_dict[i] = []

    for i in range(1, groups_number + 1):
        for j in range(1, tasks_number + 1):
            exec(f"task_dict[{i}].append('{j}_{i}')")

    free_people = []

    for i in range(1, tasks_number + 1):
        free_people.append(set(range(groups_number + 1, people_number + 1)))

    for group in range(1, groups_number + 1):
        for task in range(1, tasks_number + 1):
            chosen_people = set(random.sample(free_people[task-1], group_task_divison[group-1]))
            free_people[task-1].difference_update(chosen_people)
            for person in chosen_people:
                task_dict[person].append(f"{task}_{group}")

    return task_dict
