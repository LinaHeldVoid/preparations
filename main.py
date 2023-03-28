from stack import Stack


def check(string):
    equality = 0
    left_list = ['(', '{', '[']
    right_list = [')', '}', ']']
    answer = 'Не сбалансировано'
    some_stack = Stack(string)
    if not some_stack.is_empty():
        size = some_stack.size()
        if size % 2 == 0:
            i = 0
            k = -1
            while i < size/2:
                if string[i] in left_list and string[k] in right_list:
                    if left_list.index(string[i]) == right_list.index(string[k]):
                        equality += 1
                i += 1
                k -= 1
            if equality == size/2:
                answer = 'Сбалансировано'
    return answer


if __name__ == '__main__':
    string_for_check = '(({{[[]]}}))'
    print(check(string_for_check))
