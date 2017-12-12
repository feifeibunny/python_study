m=1
n=1
print(m)
print(n)
for i in range(3,101):
    k=m+n
    print(k)

    m=n
    n=k
    
    if i==100:
        l=m/n
        print('斐波那契数列的第99项和第100项的比值是',l)
        break
