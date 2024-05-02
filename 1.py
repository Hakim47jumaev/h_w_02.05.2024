l1=input().split()
l2=input().split()
l3=[]
odd_list=[]
none_odd_list=[]
for i in range(len(l1)):
    if i%2!=0:
        odd_list.append(l1[i])
        l3.append(l1[i])
for i in range(len(l2)):
    if i%2==0:
        none_odd_list.append(l2[i])
        l3.append(l2[i])
print(odd_list)
print(none_odd_list)
print(l3)