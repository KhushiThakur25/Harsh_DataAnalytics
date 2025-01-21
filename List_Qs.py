'''li = [23,14,5,6,47,58,65,10,61]

maxs = li[0]
secMax = 0
for i in li:
    if maxs < i:
        secMax = maxs
        maxs = i
    if maxs > i and secMax < i:
        secMax = i
print(maxs,secMax)
'''
'''
li = [1,2,3,4,5]
k = 2
while k > 0:
    end = li[len(li)-1:]
    start = li[0:len(li)-1]
    li = end + start
    print(li)
    k -= 1
'''

