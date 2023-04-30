from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox
from PIL import ImageTk,Image



def entertask():
    
    task_text = simpledialog.askstring("Add Task", "Enter a new task:")

    
    if task_text:
        listbox_task.insert(END, task_text)

def deletetask():
    
    selected_item = listbox_task.curselection()

    
    if selected_item:
        listbox_task.delete(selected_item)

def markcompleted():
    
    selected_item = listbox_task.curselection()

    
    if selected_item:
        listbox_task.itemconfig(selected_item, fg="light green")


window = Tk()
window.title("To-Do-List App")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="black", fg="green", height=10, width=40, font="Digital-7")
listbox_task.pack(side=LEFT)

entry_button = Button(window, text="Add Task", width=35, bg="green", command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete selected task", width=40,bg="red" ,command=deletetask)
delete_button.pack(pady=5)

mark_button = Button(window, text="Mark as completed", width=35,bg="dark blue",command=markcompleted)
mark_button.pack(pady=3)
img = Image.open("D:/Wallpapers/sigma.jpg")
img = img.resize((350,250)) 


photo = ImageTk.PhotoImage(img)
img_label = Label(window, image=photo,bg="black")
img_label.pack()

window.mainloop()
