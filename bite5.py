#s = "hello"
#print(s[2:] + s[:2])
#
#from collections import deque
#d = deque(s)
#d.rotate(-2)
#print(d)
    
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    dedup_names = []
    for name in names:
        if name.title() not in dedup_names:
            dedup_names.append(name.title())
    return dedup_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    fullnames, full_names = [], []
    for name in names:
        fullname = list(name.split(" "))
        fullnames.append(fullname)
    fullnames = sorted(fullnames, key = lambda n: n[1], reverse = True)
    for fn in fullnames:
        full_names.append(" ".join(fn))
 
    return full_names
 

def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    fullnames, firstnames = [], []
    for name in names:
        firstname = name.split(" ")[0]
        firstnames.append(firstname)
    first_names = sorted(firstnames, key = lambda n: len(n))
 
    return first_names[0]    




 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))