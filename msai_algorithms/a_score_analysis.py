

""" Пройтись по массиву один раз с подсчетом каждого числа, затем создать новый список и вставить соответствующее
 количество размещений  и заполнить цифрами"""

def bsearch_l(x, key):
    l = -1
    r = len(x)  
    while r-l > 1:
        m = (l+r)//2
        if x[m] < key:
            l = m
        else:
            r = m
    return l

def bsearch_r(x, key):
    l = -1
    r = len(x)
    while r-l > 1:
        m = (l+r)//2
        if x[m] <= key:
            l = m
        else:
            r = m
    return l






def process_file(filename):
    with open(filename, 'r') as f:
        N, M = map(int, f.readline().strip().split())  # N - number of students, M requests respectively
        
        if N > 0:
            scores = list(map(int, f.readline().strip().split()))  # get second line with collection of scores
            scores.sort()  # Сортируем оценки только один раз
        else:
            scores = []
        
        for _ in range(M):
            l, r = map(int, f.readline().strip().split())
            # Используем бинарный поиск для нахождения индексов
            left_index = bsearch_l(scores, l)  # Индекс первого элемента >= l
            right_index = bsearch_r(scores, r)  # Индекс первого элемента > r
            # print(right_index, left_index)
            total = right_index - left_index  # Количество студентов в диапазоне
            print(total)

# Пример использования
process_file('input.txt')
