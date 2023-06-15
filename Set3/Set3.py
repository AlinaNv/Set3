n=list(map(int,input().split()))
s=set()
for i in n:
    if i in s:
       print ("yes") 
    else:
       print("no")
       s.add(i)