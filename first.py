import qrcode
import cv2
import speech_recognition as sr
import mysql.connector
from pyzbar.pyzbar import decode

db1= mysql.connector.connect(host="localhost",user='root',password='Prome11809048',database ='qrcode')
print("Connection sucessful")

cur = db1.cursor()
s1 = input("Give a specific name for your qrcode png file :")
s2 = ".png"
s3= s1+s2
s ='INSERT INTO details values(%s,%s)'
t=(s1,s2)
cur.execute(s,t)
db1.commit()

sp_or_te =input("If you want to give a speech than press 1 or you want a text file then press 2 : ")
r = sr.Recognizer()
if sp_or_te == "1":
    with sr.Microphone() as source:
        print('speck anything : ')
        audio = r.listen(source)
        text = r.recognize_google(audio)
    print(text)
    generate_image = qrcode.make(text)
    generate_image.save(s3)

if sp_or_te == "2":
    s4 = input("Give file name : ")
    f = open(s4 ,'r')
    read = f.read()
    print(read)
    generate_image = qrcode.make(read)
    generate_image.save(s3)
    f.close()


















