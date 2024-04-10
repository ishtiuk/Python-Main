import time
schl = ['Jeremy', 'Waller', 'Zion', 'Cervantes', 'Tabitha', 'Roach', 'Heaven', 'Henry']

serach = 'Henry'

for student in schl:
    if student == serach:                         # here time Complexity = O * n = On
        print(schl.index(serach), serach)



eight = ['Jeremy', 'Waller', 'Zion', 'Cervantes', 'Tabitha']
nine = ['Roach', 'Heaven', 'Henry', 'Neveah', 'Bowers']
ten = ['Ashlynn', 'Choi', 'Brooke', 'Hardy', 'Valentino']

school = [eight, nine, ten]

search = 'Brooke'

for classs in school:
    for student in classs:                                  # here time Complexity = O * (n^2) = O n^2
        if student == serach:
            print(classs.index(student), student)
