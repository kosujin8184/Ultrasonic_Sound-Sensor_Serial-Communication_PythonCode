import serial
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import cv2
print('serial ' + serial.__version__)

# Set a PORT Number & baud rate
PORT = 'COM5'   #아두이노 포트번호
BaudRate = 9600
cnt=1

ARD= serial.Serial(PORT,BaudRate)   #시리얼 통신 변수 생성

send_alarm = "HIGH" #사운드 센서로 보내기 위한 HIGH값
send_alarm = send_alarm.encode("utf-8") #통신위해 문자열 캐스팅

def Ardread(): #아두이노로 부터 값 읽어 오기 위한 함수
    if ARD.readable():  #아두이노로부터 값 읽어오기
        LINE = ARD.readline()   #줄마다 읽기
        return int(LINE)    #정수형으로 전달
    else: 
        print("읽기 실패 from _Ardread_")
        
        
while (True):   #계속 값을 읽어오기 위해 무한루프
    
    #print(str(cnt)+"입니다. \n")
    
    Ardread()
    print(int(Ardread()))
    
    
    if((Ardread() > 20)):                 #20cm이상 떨어지면 1 전달(소리안남)
        ARD.write(1)
        cnt=1
    elif((Ardread() <= 20)&(cnt <= 3)):  #20cm 이하이면 소리가 난다. cnt=5일때 까지 소리(소리남)
        ARD.write(send_alarm)
        if(cnt > 3):
            continue
        elif(cnt <= 3):
            cnt=cnt+1
    else:                                 #cnt가 5보다 크고/ 거리가 20센치 이하가 아니면 소리안나게(소리안남)
        ARD.write(1)
        cnt=10