# file

from math import sqrt


f = open('second.txt', 'w')
for i in range(1000000):
    f.write(str(i)+' ')
f.close()
# print(f.read())

# file = open('second.txt', '+r')
# print(file.readline(2))
# file.r

# file.close()

with open('test.txt','w') as f:
    f.writelines(['Not bad', '\n\t\aand you'])

print(sqrt(4    ))

# 