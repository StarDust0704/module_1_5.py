# module_1_5.py

# 1. Задание переменной типа tuple (неизменяемая)
immutable_var = ("строка", 77, True, 3.14)
print("Кортеж immutable_var:", immutable_var)

# 2. Попытка изменения элемента кортежа
try:
    # Пытаемся изменить элемент кортежа
    immutable_var[0] = "новое значение"
except TypeError as e:
    print(f"Попытка изменить кортеж привела к ошибке: {e}")

# 3. Создание изменяемого списка
mutable_list = ["элемент 1", "элемент 2", "-55"]
print("\nСписок mutable_list до изменений:", mutable_list)

# 4. Изменение элементов списка
mutable_list[0] = "8"
mutable_list.append("333")
print("Список mutable_list после изменений:", mutable_list)

