# плохо
def get_sk(fi, pk):

    e = 10**(len(str(pk))-1)

    if len(str(pk)) != 1:
         e -= 1

    while True:
        if (e * pk) % fi == 1:
            break
        else:
            e += 2
    return e


# хорошо
def get_sk2(fi, pk):

    e = 10**(len(str(pk))-1)

    if len(str(pk)) != 1:
        e -= 1
        print("первый")
        
    while (e * pk) % fi != 1:
        e += 2
        print(e)
    print("ret")
    return e

print(get_sk2(2,1))
input()
'''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'''


# плохо
def two_simple(a, d):
    i = 2
    while i <= a:
        if a % i == 0 or d % i == 0:
            return False
        elif i == a:
            return True
        i += 1


# хорошо
def two_simple(a, d):
    i = 2
    while i <= a:
        if a % i == 0 and d % i == 0:
            return False
        elif i == a:
            return True
        i += 1


'''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'''


# плохо
def contains_spaces(str):
    result = False
    for i in str:
        if i == " ":
            result = True
    return result


# хорошо
def contains_spaces2(str):
    for i in str:
        if i == " ":
            return True
    return False
