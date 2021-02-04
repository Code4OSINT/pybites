a = ['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
b = ['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)

a = ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

a = [str(i) for i in a]

def isalpha(char):
    return (char in alpha)

def notalpha(char):
    return (char not in alpha)

#for _ in a:
#    if isalpha(a):
#        al += 1
#    result = 
    
result = [char for char in a if isalpha(char) and char != ""]

if len(result) == 1:
    print(a.index(result[0]))
else:
    result2 = [char for char in a if notalpha(char) and char != ""]
    print(a.index(result2[0]))
