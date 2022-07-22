from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os

root = Tk()
root.geometry("650x700")
root.title("Html Editor")   
root.configure(background='gray10')

open_img = ImageTk.PhotoImage(Image.open("open.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))

label_filename = Label(root,text="File Name",bg="gray19",fg="white")
label_filename.place(relx=0.28,rely=0.03,anchor=CENTER)

input_filename = Entry(root,bg="gray19",fg="white")
input_filename.place(relx=0.45,rely=0.03,anchor=CENTER)

text_area = Text(root,height=38,width=80,bg="gray19",fg="white")
text_area.place(relx=0.5,rely=0.55,anchor=CENTER) 

name = ""

def open_html():
    global name
    input_filename.delete(0,END)
    text_area.delete(1.0,END)
    
    text_file = filedialog.askopenfilename(title="Open text file", filetypes=(("html files","*.html"),))
    name = os.path.basename(text_file)
    formated_name = name.split(".")[0]
    print(name)
    input_filename.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    text_area.insert(END,paragraph)
    text_file.close()

open_button = Button(root,image=open_img,text="Open file",command=open_html)
open_button.place(relx=0.05,rely=0.01)

root.mainloop()