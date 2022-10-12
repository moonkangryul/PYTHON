def seperate():
    a = int(input('수 입력'))
    if(a%2==0):
        print('짝수')
    else:
        print('홀수')

def addResult(a,b):
    return a+b

def sum(a):
    num =0
    for i in range(1,a+1):
        num+=i
    return num

nums = [1,1,1,2,2,3,2,3,2,3,3,3,1]
def max2(nums):
    counts = {}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

def max_count(nums):
    max_count={}
    for i in nums:
        max_count[i]=nums.count(i)
    return max_count





# seperate()
# print(addResult(3,5))
# print(sum(10)) 

counts = max_count(nums)
counts2 = max2(nums)
print(counts)
print(counts2)

first = [] #list형
maxValue = max(counts.values())

for name,count in counts.items():
    print(name,":",count)
    if(count == maxValue):
        first.append(count)
print('first:',first)

