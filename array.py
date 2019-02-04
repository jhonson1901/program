w=input().split()
n=w[0]
k=w[1]
arr=[]
sum=0
for i in range(n):
  x=int(input())
  arr.append(x)
for i in range(k):
  sum=sum+arr[i]
print(sum)
