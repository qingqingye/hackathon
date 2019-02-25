import sys
import codecs
import os
import time
import audio
import serial

#xiaoji;
name= {'\xe5\xb0\x8f\xe9\xb8\xa1\xe7\x82\x96\xe8\x98\x91\xe8\x8f\x87':['20','5','0','30'],'\xe7\x95\xaa\xe8\x8c\x84\xe7\x82\x92\xe8\x9b\x8b':['5','5','0','0'],'\xe9\x9d\x92\xe6\xa4\x92\xe8\x82\x89\xe4\xb8\x9d':['3','6','0','5']}
result = ['0','0','0','0']
data = None
#yan tang weijing jiangyou
tiaoweiliao =['\xe7\x9b\x90', '\xe7\xb3\x96', '\xe5\x91\xb3\xe7\xb2\xbe', '\xe9\x85\xb1\xe6\xb2\xb9']
num =['\xe4\xb8\x80', '\xe4\xba\x8c', '\xe4\xb8\x89', '\xe5\x9b\x9b', '\xe4\xba\x94', '\xe5\x85\xad', '\xe4\xb8\x83', '\xe5\x85\xab', '\xe4\xb9\x9d', '\xe5\x8d\x81']
num2 = ['0','1','2','3','4','5','6','7','8','9']
def opentxt():
    global data
    data = open("test.txt").read()
    
def replace():
    global data

    data= data.replace('\n',',')
    for i in tiaoweiliao:
        if i in data:
            #print i
            data=data.replace(i,','+i+',')
    
    if '\xe5\x85\x8b' in data:
        data = data.replace('\xe5\x85\x8b',','+'\xe5\x85\x8b')
    
    


def split():
    global data
    data = data.split(',')


def main():
    n = 0
    start_time = time.time()
    while (n < 10):
        result = ['0','0','0','0']
        if ((time.time() - start_time)%15!=0):
            continue

        if (audio.audio2text()==False):
            continue
        n+=1
        opentxt()
        replace()
        flag = False
        for i in name:
            if i in data:
                result = name[i]
                flag = True
        
        if (flag == False):
            split()
            for i in range(len(data)):
                #print data[i]
                data[i]=data[i].replace('\xe4\xb8\x80','1')
                data[i]=data[i].replace('\xe4\xba\x8c','2')
                data[i]=data[i].replace('\xe4\xb8\x89','3')
                data[i]=data[i].replace('\xe5\x9b\x9b','4')
                data[i]=data[i].replace('\xe4\xba\x94','5')
                data[i]=data[i].replace('\xe5\x85\xad','6')
                data[i]=data[i].replace('\xe4\xb8\x83','7')
                data[i]=data[i].replace('\xe5\x85\xab','8')
                data[i]=data[i].replace('\xe4\xb9\x9d','9')
                data[i]=data[i].replace('\xe5\x8d\x81','0')
                if data[i] == '0':
                    data[i] = '10'
            for i in range(len(data)):
                if data[i] == '\xe7\x9b\x90':
                    for j in num2:
                        if j in data[i+1]:
                            result[0] = data[i+1]
                if data[i] =='\xe7\xb3\x96':
                    for j in num2:
                        if j in data[i+1]:
                            result[1] = data[i+1]
                if data[i] == '\xe5\x91\xb3\xe7\xb2\xbe':
                    for j in num2:
                        if j in data[i+1]:
                            result[2] = data[i+1]
                if data[i] == '\xe9\x85\xb1\xe6\xb2\xb9':
                    for j in num2:
                        if j in data[i+1]:
                            result[3] = data[i+1]
        
        result1 = ''
        for i in result:
            result1 += i + ' '
        
        ser = serial.Serial(port = 'COM3')
        ser.timeout = 1
        time.sleep(2)

        ser.write(result1.encode())
        ser.close()

if __name__ == '__main__':
     main()
