def remove_short_even_chains(arr):
    result = []  # Итоговый список, который будет содержать нужные элементы
    temp_chain = []  # Временный список для хранения цепочек чётных чисел

    for num in arr:
        if num % 2 == 0:  # Проверяем, является ли число чётным
            temp_chain.append(num)  # Добавляем чётное число в временную цепочку
        else:
            if len(temp_chain) >= 3:  # Если длина временной цепочки >= 3
                result.extend(temp_chain)  # Добавляем цепочку в итоговый список
            temp_chain = []  # Сбрасываем временную цепочку
            result.append(num)  # Добавляем нечётное число в итоговый список

    if len(temp_chain) >= 3:  # Проверяем последнюю цепочку на минимальную длину
        result.extend(temp_chain)  # Добавляем цепочку в итоговый список

    return result  # Возвращаем итоговый список

# Пример использования
A = [4, 3, 4, 2, 1, 2, 4, 6]
A = remove_short_even_chains(A)  # Удаляем короткие цепочки чётных чисел
print(A)  # Результат: [3, 1, 2, 4, 6]