def personal_sum(numbers):
    list_int = []
    xex_list = []
    incorrect_data = 0
    result = 0
    try:
        for i in numbers:
            if type(i) != int:
                xex_list.append(i)
            if type(i) == int:
                result += i
                list_int.append(i)
        1 / "q"
    except TypeError:
        incorrect_data = len(xex_list)
    finally:
        return result, incorrect_data, list_int

def calculate_average(numbers):
    ar = personal_sum(numbers)
    try:

        if isinstance(numbers, (list, tuple, dict, set)):
            TypeError

        if len(ar[2]) == 0 and len(ar[1]) == 0:
            ZeroDivisionError



        sred_int = ar[0] / len(ar[2])
        return sred_int

    except TypeError:
        print(" ")
        print("В numbers некорректный тип данных для подсчёта суммы")

    except ZeroDivisionError:
        print(f"Список пуст", ar)

print("~~~~~~~")
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print("~~~~~~~")
print("~~~~~~~")
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print("~~~~~~~")
print("~~~~~~~")
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print("~~~~~~~")
print("~~~~~~~")
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print("~~~~~~~")