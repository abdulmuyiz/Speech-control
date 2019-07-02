import os
from tkinter import *
import speech_recognition as sr

def onClick(event):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('speak')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            command =format(text)
        
            print(format(text))
            os.system(command)
        except:
            print('Sorry could not hear that')


root = Tk()


photo = PhotoImage(file = 'images.png')
label = Label(root,image=photo)
label.pack()
label.bind("<Button-1>" , onClick)


root.mainloop()

    

#cmd = command prompt
#notepad

