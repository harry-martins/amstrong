num=int(input())
sum=0
temp=num
while temp>0:
  rem=temp%10
  sum=sum+(rem**3)
  temp=temp//10
if num==sum:
  print("yes")
else:
  print("no")
  
