f = open('17_2024.txt')
sp = [int(i) for i in f]
m = -10 ** 10
for i in range(len(sp)):
    if sp[i] % 100 == 13 and sp[i] > m:
        m = sp[i]
k = 0
ms = -10 ** 10
for i in range(len(sp) - 2):
    k3 = 0
    if  99 < sp[i] < 1000:
        k3 += 1
    if  99 < sp[i+1] < 1000:
        k3 += 1
    if  99 < sp[i+2] < 1000:
        k3 += 1
    if k3 == 2 and sp[i] + sp[i+1] + sp[i+2] <= m:
        k += 1
        if sp[i] + sp[i+1] + sp[i+2] > ms:
            ms = sp[i] + sp[i+1] + sp[i+2]

print(k,)