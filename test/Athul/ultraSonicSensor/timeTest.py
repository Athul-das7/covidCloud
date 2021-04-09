import time
#to test the 60secs time delay
flagTime = time.time()
print(flagTime)
currentTime = time.time()
while ( currentTime - flagTime <= 60):
    print(currentTime-flagTime)
    currentTime = time.time()