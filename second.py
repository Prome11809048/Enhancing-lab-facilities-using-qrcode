import cv2
import pyzbar.pyzbar as pyzbar
import pyttsx3

text_speech =pyttsx3.init()
def decoder(frame):
    decodeObjects = pyzbar.decode(frame)
    print(decodeObjects)
    return decodeObjects

def detects_codes_on_real_time():
    import cv2
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame =cap.read()
        print(type(frame))
        decodeObjects = decoder(frame)
        if decodeObjects:
            message = decodeObjects[0].data.decode()
            x , y, w, h = decodeObjects[0].rect
            cv2.rectangle(frame, (x,y),(x+w, y+h),(255,100,20), 2)
            cv2.putText(frame,message,(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(10,20,200),2)
            print(decodeObjects[0].data)
            text_speech.say(message)
            text_speech.runAndWait()
        cv2.imshow('decoded window',frame)
        key= cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    #decoder('image.png')
    detects_codes_on_real_time()
