my_list=input().split()
chunk1=[]
chunk2=[]
chunk3=[]
for i in range(len(my_list)//3):
    chunk1.append(my_list[i])
for i in range(len(my_list)//3,(len(my_list)*2)//3):
    chunk2.append(my_list[i])
for i in range(len(my_list)*2//3,len(my_list)):
    chunk3.append(my_list[i])
 
print("chunk1 ->",chunk1)
chunk1.reverse()
print("After reverzing it :",chunk1)

print("chunk2 ->",chunk2)
chunk2.reverse()
print("After reverzing it :",chunk2)
print("chunk3 ->",chunk3)
chunk3.reverse()
print("After reverzing it :",chunk3)