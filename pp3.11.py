print('Saifullah,18B-092-CS, A')
print('Assignment # 3')
print('Practice problem 3.11')
# function, returns all even integers in list.
def allEven(lst):
    'Returns true if all integers are even, otherwise false'
    for x in lst:
        if (x%2) != 0:
            return False

    return True
    
