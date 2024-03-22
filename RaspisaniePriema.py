'''Составить расписание приёма врача с 9:00 до 21:00, состоящее из 30-минутных промежутков
и с учётом перерывов на кварцевание и прочее. Расписание перерывов приёма дано в списке busy'''

busy = [
{'start' : '10:30',
'stop' : '10:50'},
{'start' : '18:40',
'stop' : '18:50'},
{'start' : '14:40',
'stop' : '15:50'},
{'start' : '16:40',
'stop' : '17:20'},
{'start' : '20:05',
'stop' : '20:20'}
]

l=len(busy)
nachs=[]
kons=[]
n=0
while n<l:
    nachalo=busy[n]['start']
    nach=int(nachalo[0])*10+int(nachalo[1])+(int(nachalo[3])*10+int(nachalo[4]))/60
    konec=busy[n]['stop']
    kon=int(konec[0])*10+int(konec[1])+(int(konec[3])*10+int(konec[4]))/60
    nachs.append(nach)
    kons.append(kon)
    n+=1

nachs.sort()
kons.sort()

def funk(ar):
    chas=int(ar // 1)
    chas=str(chas//10)+str(chas%10)
    min=int(round((ar - ar // 1) * 60))
    min=str(min//10)+str(min%10)
    return chas + ':' + min

n=0
rasp=[]
x=9
while x<21 and n<=l-1:
    if x + 0.5 <= nachs[n]:
        y=x
        x+=0.5
        nach=funk(y)
        kon=funk(x)
        z={'start':nach, 'stop':kon}
        rasp.append(z)
    elif x+0.5 >= nachs[-1] and x+0.5<=21:
        x=kons[-1]
        y = x
        x += 0.5
        nach = funk(y)
        kon = funk(x)
        z = {'start':nach, 'stop':kon}
        rasp.append(z)
    else:
        x=kons[n]
        n+=1

l=len(rasp)
n=0
while n<l:
    print("с", rasp[n]['start'], "до", rasp[n]['stop'])
    n+=1