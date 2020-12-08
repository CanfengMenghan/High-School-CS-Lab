import time
while True:
    time0=float(time.time())
    currenttime=0
    while True:
        pasttime=int(float(time.time())-time0)
       # print(pasttime)
    
        if pasttime!=int(currenttime):
            currenttime=pasttime
            print(pasttime)
        
