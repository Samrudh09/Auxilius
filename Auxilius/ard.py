import serial
arduinoSerialData=serial.Serial()
arduinoSerialData.port='COM3'
arduinoSerialData.open()
while True:
    if (arduinoSerialData.inWaiting()>0):
        myData=(arduinoSerialData.readline())
        print myData


