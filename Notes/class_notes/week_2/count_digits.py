# n = 939348
# n = str(n) # "939348"

# count = 0
# for i in range(len(n)):
#     count += 1

# print(count)


'''
count += 1    -->   count = count + 1
'''

n = 523
count = 0
while n != 0:
    # print(n)
    n = n//10
    count = count  + 1    

print(count)
# stop when the n = 0