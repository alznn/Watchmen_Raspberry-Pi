import serial
from firebase import firebase
from firebase_admin import db
last = None
firebase = firebase.FirebaseApplication("https://watchmen-app.firebaseio.com/")
class RMC:
   def __init__(self, arr):
   ¦   self.time = arr[1]
   ¦   self.latitude = arr[3] + arr[4]
   ¦   self.longitude = arr[5] + arr[6]
   ¦   self.date = arr[9]

 def getdata(port):
 # open the serial port
     port.open()
 # check that the port is open
     if port.isOpen():
 # read 16 lines
     ¦   line = []
     ¦   for i in range(0,9):
     ¦   ¦   line.append(port.readline())
 # close the serial port
     port.close()
 # discard the first line (sometimes it contains rubbish, so just always discard it)
     del line[0]
 # return the list of lines
     return line

 def outputdata(data):
                                                                                                                  buffers
 #    Counting(last , data)
 # print the list of lines
     for i in range(0,len(data)):
     ¦   nowdata = data[i].split(",")
     ¦   if nowdata[0] == '$GPRMC':
     ¦   ¦   last = RMC(nowdata)
     ¦   ¦   print(last.time)QW

 #def Counting(last , current):
 #    print ("Here is count : "+ current[0]-last[0])

 def FireBaseConnection(setX,setY,DrivingTime):
     re = firebase.put('DrivingInfo',"Time",DrivingTime)
     rs = firebase.get('/DrivingInfo/Time',None)
 #    re = firebase.put("alert","user","abcdefg")
 #    rs = firebase.get("alert/user",None)
     print(rs)


 def initialise():
 # initialise serial port settings
     Port = serial.Serial()
     Port.baudrate = 9600
     Port.port = '/dev/ttyACM0'
     Port.xonxoff = 1
 # return the port as an object we can use
     return Port

 # main program starts here
 sPort = initialise()
 while True:
     data = getdata(sPort)
     print("====================")
     outputdata(data)
     print("<++++++++++++++++++>")

#FireBaseConnection("50.0N","50.0E","55")
# end