print("cek")

def kata(n):
    for i in n:
        print(i, end=" - ")
        if i % 2 == 0:
            print("Berkualitas")
        elif i % 3 == 0:
            print("I Love Coding")
        else:
            if i % 1 == 0:
                print("Santai")


#x=[1,2,3,4,5]
p=20

n=[]
for j in range(p):
    j+=1
    n.append(j)

print(n)

kata(n)
