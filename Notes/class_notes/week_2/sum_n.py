#sum of n natural numbers
'''
1+2+3+4
'''

# given n = 4 
# output = 10

# 1 -->  1
# 2 -->  3
# 3 -->  6
# 4 -->  10

#range(start,end)
#range(10)


n = int(input())
load = 0
for i in range(1,n+1): # 1 2 3 4
    load += i

# load + i = load
# 0    + 1 = 1
# 1     + 2 = 3
# 3     + 3 = 6
# 6     + 4 = 10

print(load) #10











