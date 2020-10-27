import time

endCount = 5   #number of times to count
delayTime = 1   #Time for each delay (in seconds)

#If we want to count up every x seconds, there are a couple of ways to do it.

#Method 1: time.sleep
#time.sleep() is blocking. What this means is that when you use time. sleep() ,
#you'll block the main thread from continuing to run while it waits for the sleep() call to end.

counter = 0;
while True:               #Create a never-ending loop
    if counter < endCount:
        counter += 1;
    else:
        break

    print(counter, end='... ')
    time.sleep(delayTime) #pauses the execution of the ENTIRE PROGRAM
    #Due to it's blocking method using time.sleep isn't always optimal if you want to do anything else at the same time
    time.time()
    
    
#Method 2 - Storing a time.time() value
print('\r\nCurrent Time = ', time.time())
futureTime = time.time() +  delayTime #Set the
print(futureTime)


counter = 0;
while True:               #Create a never-ending loop
    
    if futureTime < time.time():
        if counter < endCount:
            counter += 1;
            futureTime = time.time() + delayTime
        else:
            break
        print(counter, end='... ')
    
    #Almost the exact same functionality EXCEPT this method is non-blocking
    #print(time.time())

