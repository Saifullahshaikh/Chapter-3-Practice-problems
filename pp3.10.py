print('Saifullah,18B-092-CS, A')
print('Assignment # 3')
print('Practice problem 3.10')
#function for novowel
def noVowel(s):
    'Returns true if there is no vowel in string'
    for a in s:
        if a in 'aeiouAEIOU':
            return False
    return True
        
