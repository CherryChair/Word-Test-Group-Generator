import random


def input_numbers():
    while True:
        try:
            people_number = int(input("Ile jest osób w klasie: "))
            if people_number <= 0:
                print("Liczba osób w klasie musi być dodatnia.")
                continue
            groups_number = int(input("Ile jest grup: "))
            if groups_number <= 0:
                print("Liczba grup musi być dodatnia.")
                continue
            tasks_number = int(input("Ile jest zadań: "))
            if tasks_number <= 0:
                print("Liczba zadań musi być dodatnia.")
                continue
            group_task_divison = []
            for group in range(1, groups_number + 1):
                group_task_divison.append(int(input(f"Ile osób dodatkowo ma dostać zadanie z grupy {group}: ")))
            if any([group_task_divison[i] < 0 for i in range(0, groups_number)]):
                print("Liczba dodatkowo przydzielonych zadań z grupy musi być nieujemna.")
                continue
            break
        except Exception:
            print("To nie jest liczba")
    info_table = []
    info_table.append(people_number)
    info_table.append(groups_number)
    info_table.append(tasks_number)
    info_table.append(group_task_divison)
    if sum(group_task_divison) + groups_number != people_number:
        print("Liczba zadań przydzielonych z poszczególnych grup nie jest równa liczbie osób w klasie.")
        info_table = input_numbers()
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
