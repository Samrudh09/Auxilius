from flask import Flask, request , render_template
from os import system
import os
import pandas as pd
import glob
import time

'''

Packages Required:

pandas
flask
glob if not already pre-installed




Folder layout:
    Auxilius:  server_listenV2.py 
               notifier.py
               user_input_pres.csv
               Medicines(Folder) : Med1.txt
                                   Med2.txt 

'''


'''

Sample inputs from the url:

http://0.0.0.0:5000/?scan=Med1,2,8   notify Med1 every 2 seconds 8 times
http://0.0.0.0:5000/?scan=Med1,4,5   notify Med1 every 4 seconds 5 times
http://0.0.0.0:5000/?scan=Med2,30,3  notify Med2 every 20 seconds 3 times


The QR code text should be ?scan=Med1,2,8 , ?scan=Med1,4,5 , ?scan=Med2,30,3

!!change the directories is lines 73,74 in this code and 8 and 11 in Notifier.py!!


'''
#This has to be run from the terminal (after changing directory using cd to the current folder ) : python server_listenV2.py
# from multiprocessing import Process

import datetime 
# change directories for the Rasp Pi

Users=[]
Medicine_list=[]
Notification_list=[]


app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def result():

    arguments_1 = request.args.get("scan") # will get all parameters after scan 
    print arguments_1
    if request.method=='POST':
        post_data=request.data
        print post_data


    patient_name="Adam"
    time_stamp_start=str(datetime.datetime.now()) #time stamps the request it receives
    time_stamp_exp=str(datetime.datetime.now()) #this will change later for now it is just dummy data
    string_input=[patient_name,time_stamp_start,arguments_1,time_stamp_exp] # converts the input from browser and time stamps to a list
    append_string=",".join(string_input) # converts all inputs to a string (comma separated values for .csv)
 
    with open("user_input_pres.csv", "a") as myfile: #appends these values to a .csv file
        myfile.write(append_string)
        myfile.write("\n")

    temp_1=append_string.split(',')
    print temp_1[2]
    if len(glob.glob("/Users/Samrudh/Desktop/Auxilius/Medicines/%s.txt"%str(temp_1[2]))) > 0: # str(temp_1[2]) will be 'Med1' or 'Med2' , This will check if suck a file exists or nah
        files__=glob.glob("/Users/Samrudh/Desktop/Auxilius/Medicines/%s.txt"%str(temp_1[2]))
    

        with open(files__[0],'w') as f: #files__[0] is the name of the .txt file in the medicines folder
            f.write(append_string)
            f.write("\n")

    if temp_1[2]=='Med1': #Which Medicine will the notification be sent for 
        notif_=1 # these will be used as a external parameter passed to the notifier.py eg: python notifier.py 1
    else:
        notif_=2
    print notif_

    df=pd.read_csv('user_input_pres.csv') # this is a convreting the .csv file to a dataframe (its database-ish) this is done using the pandas library 
    input_table=(df.to_html()) # im converting the dataframe into a html table code and then adding it the base html code

    return '''
    <!doctype html>

<html>
    <head>
        <title>

            
        Auxilius
        
        </title>
    </head>
    <body>
        <h1><center>Auxilius Notification Dashboard</center></h1>
    <!--<h1>,<h2> are the different sized headers you can use sa you widh-->
    <h2><center>Presciptions Scan History</center></h2>
<center>%s</center>

</body>
</html>

    ''' %input_table , os.system("python Notifier.py %s &"%str(notif_)) # This will either run a notification for Med1 or Med2

def Listener():

    while True:
        app.run(host="0.0.0.0",threading='True') # dont change this 


if __name__=='__main__':
    Listener()

'''Application to be run in the terminal'''




    




















