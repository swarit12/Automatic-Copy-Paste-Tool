from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import asksaveasfilename
import pyperclip
import threading
import time

root= Tk()

root.geometry("550x615")
root.title("Copy/paste tool")


def thread():
    t = threading.Thread(target=start_copying)
    t.start()

def start_copying():
    start_button.config(text= "STARTED PASTING")
    pyperclip.copy("")
    recent_value = ""
    while True:
        temp_value= pyperclip.paste()
        if temp_value!= recent_value:
            recent_value=temp_value
            text.insert(END, pyperclip.paste())
            text.insert(END, "\n")
        time.sleep(0.1)

def save():
    save_button.config(text= "SAVING...")
    file= asksaveasfilename(title= "Save your file", filetypes=(("text file", "*.txt")
                                                               , ("all files","*.*")))
    if file:
        f= open(file, "w")
        copied_text= text.get(1.0, END)
        f.write(copied_text)
        f.close()
    save_button.config(text= "SAVE")

heading= Label(root, text="AUTOMATIC", font=("Monotype Corsiva", 37,
"italic")).grid(row= 0, padx= 100)
heading2= Label(root, text= "COPY/PASTE",fg= "deep sky blue",font=
 ("Monotype Corsiva", 40, "bold italic")).grid(padx= 50)

start_button= Button(root, text= "START PASTING >>", bg= "#20bebe",fg= "white",borderwidth= 1,
width= 20, height= 3,font= ("", 10, ""), command=thread)
start_button.grid(pady= 15)

text= scrolledtext.ScrolledText(root,width= 60, height= 20)
text.grid(pady= 12, padx= 35)

save_button= Button(root, text= "SAVE",bg= "#20bebe",fg= "white", font=("",10, ""),width= 11, borderwidth= 2,command= save)
save_button.grid(row= 5, ipady= 5, padx= 10)


root.mainloop()