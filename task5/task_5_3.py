# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("text_3.txt", "r", encoding="utf-8") as file:
    text = file.readlines()
    print(f"Исходный текст: {text}")
    value = 0
    for i in range(0, len(text)):
        text[i] = text[i].rstrip("\n").split()
        if float(text[i][1]) < 20000:
            print(f"У {text[i][0]} зарплата менее 20000")
        value += float(text[i][1])
    print(f"Средняя зарплата сотрудников равна: {value / len(text)}")
