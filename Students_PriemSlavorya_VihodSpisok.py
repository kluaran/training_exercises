kol=int(input("Введите количество студентов: "))
x={}
for t in range(kol):
    x['Студент №'+str(t+1)]=input('Студент №'+str(t+1)+' ')
spisok=[]
for name in x.values():
    spisok.append(name)
spisok.sort()
print(spisok)