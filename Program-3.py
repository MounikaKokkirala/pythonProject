n=int(input("Enter the number: "))
if(n%2==0):
    n=n-1
count=1
initial_number=1
odd_number_series=[]
while count<=n:
    odd_number_series.append(initial_number)
    initial_number+=2
    count+=1
print(odd_number_series)