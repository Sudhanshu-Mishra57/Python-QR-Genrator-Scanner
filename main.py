# Importing required modules
#first import pyqrcode and pypng
#install pyzbar
#install opencv-python

from tkinter import *
root=Tk()
import cv2
import pyqrcode
from pyzbar.pyzbar import decode
from warnings import filterwarnings
filterwarnings('ignore')
root.geometry('400x200')
root.title('Choose your size')


def button_connand():
    content = entry.get()
    #with open("txt") as f:
    #    content = f.read()
    url = pyqrcode.create(content)
    url.png("myfile22.png",scale=5)
    print("success")

entry = Entry(root,width = 20,)
entry.pack()

def scan():
    # Capture the video from default camera
    capture = cv2.VideoCapture(0)
    
    print("Escape Key (Esc) to exit...")
    print('------------------------------------------------------------------------------\n')
    
    recieved_data = None
    while True:
        # reading frame from the camera
        _, frame = capture.read()
        # Decoding the QR Code 
        decoded_data = decode(frame)
        try:
            data = decoded_data[0][0]
            if data != recieved_data:
                recieved_data = data
                print("\n", data, "\n")
        except:
            pass
        
        # Showing video.
        cv2.imshow("QR CODE Scanner", frame)
    
        # To exit press Esc Key.
        key = cv2.waitKey(1)
        if key == 27:
            break
#================================#
   ####### Buttons ###########
button_1 = Button(root,text="QR Generate",command=button_connand,width = 20,height=2).pack()
button_2 = Button(root,text="QR Scanner",command=scan,width = 20,height=2).pack()
root.mainloop()