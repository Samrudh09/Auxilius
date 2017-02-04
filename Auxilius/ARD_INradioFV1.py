import serial
import webbrowser
arduinoSerialData=serial.Serial(timeout=1)
arduinoSerialData.port='COM3'
arduinoSerialData.open()
print("Hello Welcome to the automated Internet Radio !!")
print("Please select from the available radio streams :")
print('The available channels are listed \t\n1.(62.4)-Weather Radio Canada\t\n2.(90.3)-Toronto Classic\t\n3.(96.3)-The New Classic FM')
while(1==1):
    #print arduinoSerialData.readline()
    user_RADinput=arduinoSerialData.read()
    for i in user_RADinput:
        input_list=[]
        input_list.append(int(i))
        #print i
        new1=2
        if int(i)==1:
            url="http://audioplayer.wunderground.com:80/Tundraeh/innisfil.mp3"
            print("NOW Playing:Weather Radio Canada.........")
            webbrowser.open(url,new=new1)
        elif int(i)==2:
            url="http://7otor0.akacast.akamaistream.net/7/321/177415/v1/rc.akacast.akamaistream.net/7OTOR0"
            webbrowser.open(url,new=new1)
            print("NOW Playing:Toronto Classic.........")
        elif int(i)==3:
            url="http://65.19.131.138/mzmedia-cfmzfmmp3-ibc2?session-id=1620376281&source=tunein"
            webbrowser.open(url,new=new1)
            print("NOW Playing:The New Classic FM.........")
