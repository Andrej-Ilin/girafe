def find_str(s, sub):
    """Находит индекс первого вхождения подстроки `sub` в строке `s`.
    Возвращает -1, если подстрока не найдена."""
    s_len = len(s)
    sub_len = len(sub)

    # Перебираем все возможные позиции для поиска подстроки
    for i in range(s_len - sub_len + 1):
        # print(i)
        # Сравниваем символы строки s с символами подстроки sub
        match = True
        for j in range(sub_len):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            return i  # Возвращаем индекс, если подстрока найдена

    return -1  # Возвращаем -1, если подстрока не найдена


def find_circular_shift(s1, s2):
    if len(s1) != len(s2):
        return -1

    # Создаем строку, которая содержит s1 дважды
    s1s1 = s1 + s1

    # Находим индекс s2 в s1s1
    index = find_str(s1s1, s2)

    if index != -1:
        # Если s2 найден, то K будет равно длине строки минус индекс
        return len(s1) - index if index != 0 else 0

    return -1


if __name__ == '__main__':
    import sys
    sys.stdin = open('input.txt', 'r')
    s1 = input().strip()
    s2 = input().strip()
    print(find_circular_shift(s1, s2))
