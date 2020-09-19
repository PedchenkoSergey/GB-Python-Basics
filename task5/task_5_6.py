# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

edu = {}

with open("text_6.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
    for i in range(0, len(content)):
        content[i] = content[i].rstrip("\n").split()
        edu[content[i][0].rstrip(":")] = 0
    print(f"Считанная из файла строка: {content}")
    print(f"Получившийся исходный словарь: {edu}")
    for i in range(0, len(content)):
        for j in range(1, len(content[i])):
            try:
                edu[content[i][0].rstrip(":")] += int(content[i][j][0:content[i][j].index("(")])
            except ValueError:
                pass
    print(f"Итоговый словарь: {edu}")
