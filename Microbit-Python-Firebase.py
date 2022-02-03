# Firebase Database URL
# https://lccsproject2022-default-rtdb.europe-west1.firebasedatabase.app/
# Get the url as shown above for your database, check the guide.
# Created new database on 15-12 as old one only lasted 30 days...

# NOTE - This is to test and ensure that the microbit is working with python via serial lin
# Code for firebase has been commented out as the database is out of date..
# to make this work with firebase a new database should be created..

import serial
import time
import datetime

#from firebase import firebase

#myDBConn = firebase.FirebaseApplication('https://lccsproject2022-default-rtdb.europe-west1.firebasedatabase.app/', None)

serCon = serial.Serial()
serCon.baudrate = 115200
serCon.port = "COM10" # This can sometimes change # easiest way to determine is use device manager and check for com ports.
serCon.open()
print("SUCCESS WE HAVE GOT THIS FAR ")

while True:
    microbitData = str(serCon.readline())
    
    temp = microbitData[2:] # slice string from pos 3 to the end of the string
    #Remove spaces from the string
    temp = temp.replace(" ","")
    #Replace the escape characters with an empty char using the replace function()
    temp = temp.replace("\\r\\n","")
    #replace the ' character with ""
    temp = temp.replace("'","")
    #convert the string to an int
    temp = int(temp)
    
    print(temp)
    

    #now = datetime.datetime.now()
    
    now = int(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))# %Y%m%d%H%M%S formats year month day hour min sec
    print(now)
    
    record = {
     "temp" : temp,
     "timeStamp" : now 
    }
    
    print(record)

    #result = myDBConn.post("temperature", record)
    #print the unique id that is returned from the firebase database
    #print(result)
    
    time.sleep(5)
 
serCon.close()
#myDBCon.close()
    
