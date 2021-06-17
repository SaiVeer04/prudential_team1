import matplotlib
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

import gspread
import time
import os
import sys
from google.oauth2.service_account import Credentials
gc = gspread.service_account("Creds.json")

sh = gc.open_by_key('1CRGs_BX755_oOsR52V2KdrJTd_4ximXcQjZx_w7JJOU')

worksheet = sh.sheet1



def profit():
    f = open("Startup.txt", "w")
    for x in range(3,262):
        res = str(worksheet.get('AG'+str(x)))
        hold = res
        test = hold.replace("[['","")
        test1 = test.replace("']]","")

        if(test1 == "Yes"):
            f.write(str(x) + "\n")
            print("Works")
        if(x%60==0):
            time.sleep(60)
        print(str(x)+" "+test1)
    f.close()
#profit()

def save_data(column):
    print("working..." + column)
    count = 0
    f = open(f"{column}.txt","w")
    f1 = open('Startup.txt', 'r')
    lines = f1.readlines()
    for line in lines:
        record = int(line.strip())
        res = str(worksheet.get(column + str(record)))
        hold = res
        test = hold.replace("[['", "")
        test1 = test.replace("']]", "")
        if (count % 50 == 0):
            time.sleep(60)
        count = count + 1
        f.write(test1+"\n")
        print(count)
    f.close()

def get_data(column):
    #Gettting the x-value
    revenue = []

    f1 = open(f'{column}.txt','r')
    f = open('Startup.txt', 'r')
    revenue_have = False
    lines = f1.readlines()
    lines1 = f.readlines()
    count = 0
    for line in lines:
        revenue_have = False
        record = str(line.strip())
        res = record


        #print(res)
        if(len(revenue) > 0):
            for x in revenue:
                if(x.find(res) > -1):
                    revenue_have = True
            if(revenue_have == False):
                revenue.append(res)
        else:
            revenue.append(res)
        count = count + 1


    y_pos = np.arange(len(revenue))

    length = len(revenue)
    performance=[]
    for x in range(0,length):
        performance.insert(x,0)
    count = 0
    print(performance)
    for line in lines:
        record1 = str(line.strip())

        for x in range(0,length):
            if(revenue[x] == record1):
                performance[x] = performance[x]+1

    hold = worksheet.get(column + "2")
    test = str(hold).replace("[['", "")
    test1 = test.replace("']]", "")
    print(test1)
    print("X Values: " + str(revenue))
    print("Y Values: " + str(performance))

    font = {'size':6}

    plot1 =plt.figure(1)
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, revenue)
    hold = worksheet.get(column + "2")
    test = str(hold).replace("[['", "")
    test1 = test.replace("']]", "")
    plt.ylabel('Usage')
    plt.title(test1)
    matplotlib.rc('font',**font)

    plot2=plt.figure(2)
    plt.pie(performance, labels=revenue, autopct='%1.1f%%')

    plt.title(test1)
    plt.axis('equal')
    matplotlib.rc('font', **font)
    plt.show()






#save_data("E")
get_data("AB")


