#Bir listedeki 10 dadn büyük sayıları bulan program.

import random

list = []
count = 0
for i in range(20) :
    number = random.randint(1,20)
    list.append(int(number))

for i in range(len(list)) :
    if(list[i] > 10):
        count+=1
     
print("Listedeki 10'dan büyük sayılar :",count)