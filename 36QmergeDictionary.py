d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}


for i in d2:
    d1[i] = d2[i]

print(d1)

d1 = {10:100,20:200,40:300}
sum = 0

for i in d1:
    sum = sum + d1[i]

print(sum)



