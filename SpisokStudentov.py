'''Создание списка студентов в алфавитном порядке'''

spisok=[]
y=''
names=input('Введите Имена студентов через запятую и пробел: ')
l=len(names)

for x in range(l):
    if (names[x]==',' and names[x-1]!=',' and names[x-1]!=' ' and x!=0) or (names[x]==' ' and names[x-1]!=',' and names[x-1]!=' ' and x!=0):
        spisok.append(y)
        y=''
    elif (names[x]==',' and (names[x-1]==',' or names[x-1]==' ')) or (names[x]==' ' and (names[x-1]==',' or names[x-1]==' ')):
        continue
    elif x==l-1 and names[x]!=',' and names[x]!=' ':
        y = y + names[x]
        spisok.append(y)
    elif x==0 and (names[x]==',' or names[x]==' '):
        continue
    else:
        y=y+names[x]

print("Вы не ввели ни одного Имени") if spisok==[] else print("Список студентов:")
spisok.sort()

l=len(spisok)
spisok_full={}
for x in range(l):
    spisok_full['Студент №'+str(x+1)]=spisok[x]
for x in spisok_full.items():
    print(x)
