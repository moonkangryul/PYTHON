a = 2
if(a==1):
    print(1)
print(2)

if(a==1):
    print(1)
elif(a==2):
    print(2)
else:
    print(3)



print(1 in [1,2,3])
print(1 not in [1,2,3])
print('i' not in 'python')

money = 1200

if money < 10:
    pass
else:
    print('저금')

#반복문
for i in [1,2,3]:
    print(i ,end = ' ')
print('\n')
for i in (1,2,3,):
    print(i,end = ' ')
print('\n')

for i in 'Hello':
    print(i,end=' ')
print('\n')

for i in ['one','two','three']:
    print(i,'!')

num = 10
while(num > 0):
    if(num == 6):
        print(end = '---end---')
        break
    print(num,end =' ')
    num-=1

print()
for i in range(10):
    print(i,end=' ')
print()

num = 0
sum = 0
while(num < 100):
    if(num !=0 | num%7 == 0):
        sum += num
        print(num,end=' ')
    num += 1
print('\n',sum)

for i in range(3):
    for a in range(3):
        print('*',end = ' ')
    print()
print() 
i=0
while i<5:
    i += 1
    print('*'*i)
print()