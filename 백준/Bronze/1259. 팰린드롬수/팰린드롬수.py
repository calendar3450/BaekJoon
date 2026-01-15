while True:
    n = input()
    if n == '0':
        break
    arr = list(n)
    rev_arr=list(reversed(arr))
    if arr == rev_arr:
        print('yes')
    else:
        print('no')