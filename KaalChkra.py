import time
m=0
h=0
s=1
while True:
    time.sleep(1)
    print(h,":",m,":",s)
    s+=1
    if s==60:
        s=1  #________________________________After 60 Second code will be forget____
        m+=1
    if m==60:
        h+=1
        m=0
# Timer complete. 
