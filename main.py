from telnetlib import Telnet
from datetime import datetime, time
import sys

args = list(sys.argv)[1:]


clicked1 = False
clicked2 = False

def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime


def _request(request):
        con.write(('%s\n' % request).encode('ascii'))
        response = con.read_some().decode('ascii').strip()
        con.write('c\n'.encode('ascii'))
        return response

def start_recording():
    return _request('AOS')

def stop_recording():
    return _request('LOS')

con = Telnet("localhost",4532,4)

print("SCHEDULED PASS TO RECORD: \nAOS: "+str(int(args[0]))+":"+str(int(args[1]))+"\nLOS: "+str(int(args[2]))+":"+str(int(args[3])))

while True:
    t = datetime.now()
    if t.hour == int(args[0]) and t.minute == int(args[1]) and clicked1 == False:
        start_recording()
        clicked1 = True
        print("RECORD START")
        
    if t.hour == int(args[2]) and t.minute == int(args[3]) and clicked1 == True and clicked2 == False:
        stop_recording()
        clicked2 = True
        print("RECORD END")
    
