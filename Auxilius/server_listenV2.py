from flask import Flask, request , render_template
from os import system
import pandas as pd
import numpy as np
import time
from multiprocessing import Process

import datetime

FMT = '%d:%m:%Y:%H'
Users=[]
Medicine_list=[]
Notification_list=[]


app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def result():
    # if request.method == 'POST':  
    arguments_1 = request.args.get("scan")
    print arguments_1

    with open("user_input_pres.csv", "r") as myfile:
    	patient_name="P1"
    	time_stamp_start=str(datetime.datetime.now())
    	time_stamp_exp=str(datetime.datetime.now())
    	string_input=[patient_name,time_stamp_start,arguments_1,time_stamp_exp]
    	append_string=",".join(string_input)
 
    with open("user_input_pres.csv", "a") as myfile:
    	myfile.write(append_string)
    	myfile.write("\n")

    temp_1=append_string.split(',')
    print temp_1[2]
    if temp_1[2] in Medicine_list == True:
        print 'Already There'
    else:
        Medicine_list.append([temp_1[2]])
        print 'appended'



    df=pd.read_csv('user_input_pres.csv')
    input_table=(df.to_html())

    # with open('/Users/Samrudh/Desktop/Auxilius/templates/my_file.html', 'w') as fo:
    # 	fo.write(df.to_html())


    	    # system(' say Medicine 1 dosage %s times a day'% searchword_1)
    
   
    # return render_template('Aux_index.html')
    # return render_template('my_file.html')
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
    <h2><center>Presciptions</center></h2>
    <p>The following precriptions have been scanned by the user:</p>
    
<center>%s</center>

</body>
</html>

    ''' %input_table
 
if __name__ == '__main__':
    app.run(host="0.0.0.0")

def Listener():

    while True:
        app.run(host="0.0.0.0")

# def Notification():

if __name__=='__main__':
    Process(target=Listener).start()
    # Process(target=Notification).start()




















