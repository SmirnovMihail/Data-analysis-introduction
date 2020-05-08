def brackets(n, open_brackets=0, close_brackets=0, ans=''):
    if open_brackets + close_brackets == 2 * n:
        yield ans
    if open_brackets < n:
        yield from brackets(n, open_brackets + 1, close_brackets, ans + '(')
    if close_brackets < open_brackets:
        yield from brackets(n, open_brackets, close_brackets + 1, ans + ')')
        
if __name__ == '__main__':
    n = int(input())
    [print(i) for i in brackets(n)]