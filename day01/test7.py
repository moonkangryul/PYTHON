# f=open('c:/test/새파일. txt','w')
# print(f)
# f.close()

f=open('c:/test/새파일. txt','w')
for i in range(1,6):
    data = '%d번째 줄입니다. \n' %i
    f.write(data)

f.close()

f=open('c:/test/새파일. txt','a')
for i in range(6,11):
    data = '%d번째 줄입니다. \n' %i
    f.write(data)


    

f.close()


f=open('c:/test/새파일. txt','r')
line = f.readline()
print(line)

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()


f=open('c:/test/새파일. txt','r')
line = f.readlines()
print(line)
f.close()

f=open('c:/test/새파일. txt','r')
data = f.read()
print(data)
f.close()

with open('c:/test/새파일. txt','w') as f: #close() 포함
    f.write['aa bb cc']
# data = f.read() 오류발생 : f 가 close 된 상태임

