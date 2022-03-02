
#Challenge 1

num = 1

while num < 11:
    print(num)
    num += 1


#Challenge 2

chosenNum = input('Enter a number: ')
modifier = 1
chosenNum = int(chosenNum)

for count in range(1, chosenNum, 1):
    chosenNum += count

print (chosenNum)


#Challenge 3

for count in range(1500, 2701, 1):
    if (count % 7 == 0 and count % 5 == 0):
        print (count)


#Challenge 4

for count in range(1, 6, 1):
    
    for num in range (1, count, 1):
        print(num, end ="")
    print(count)


#Challenge 5

num1 = input('Enter a number: ')
print(len(num1))

    #Looping method
n=int(input("Enter a number: "))
count=0
while(n>0):
    count=count+1
    n=n//10
print(count)


#Challenge 6
rangeMin = int(input('Enter a range min: '))
rangeMax = int(input('Enter a range max: '))

def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

for integer in range(rangeMin, rangeMax + 1, 1):
    if isprime(integer):
        print(integer)

