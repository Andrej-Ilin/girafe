import sys

def sequence(N):
    """берем последовательность из N элементов удаляем последнеес значение и
     добавляем его в новый список до тех пор пока не дойдем до зеркальных скобок,
      если появляется зеркальная скобка удаляем ее из нового списка. """
    matching_bracket = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for element in N:
        if element in matching_bracket.values():
            stack.append(element)
        elif element in matching_bracket.keys():
            if stack and  matching_bracket[element] == stack[-1]:
                stack.pop()
            else:
                return 'no'
    return 'no' if stack else 'yes'

if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    N = list(input().strip())
    print(sequence(N))