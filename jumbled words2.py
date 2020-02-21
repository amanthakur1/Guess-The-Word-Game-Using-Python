# imorting all the modules
import tkinter
from tkinter import *
import random
from tkinter import messagebox
# list which contain the answers of the word which we have to guess
answers=[
 'delhi',
 'mumbai',
 'kolkata',
 'chennai',
 'vizag',
 'jaipur',
 'lucknow',
 'kanpur',
 'bangalore',
 'python',
 'java',
 'html',
 'swift',
 'apple',
 'samsung']
# words diplayed on the screen for which we have to give answer
words=[
 'ehdli',
 'bumaim ',
 'takolak',
 'nhnceai',
 'gazvi',
 'purija',
 'koclwnu',
 'ankpru',
 'gabanrelo',
 'nthyop',
 'ajva',
 'thlm',
 'wisft',
 'papel',
 'gusamns']

# random number storing
num=random.randrange(0,15,1)
# function that configure the random words in label
def working():
    global words,answers,num
    lbl.config(text=words[num])
# function which check that entered answer is correct or not
def checkans():
    global words,answers,num
    var = e1.get() # provide vale to var from entry box
    if var == answers[num]:
        messagebox.showinfo("CORRECT","This is correct answer")
        res()
    else:
        messagebox.showerror("ERROR","This is not a correct answer")
        e1.delete(0,END)
# function which reset the label value when one answer is given or when reset button is pressed
def res():
    global words,answers,num
    num=random.randrange(0,15,1)
    lbl.config(text=words[num])
    e1.delete(0,END)


#defining the tkinter and provinding attributes to tkinter
root = tkinter.Tk()
root.geometry("400x500")
root.title("GUESS THE WORDS")
root.configure(background="#000000")



# defining label box ,which show the jumblled word on the screen
lbl= Label(
    root,
    text="Shivam Yadav",
    font=("verdana",18),
    bg="#000000",
    fg="#ffffff",
)
lbl.pack(pady=30,ipady=10,ipadx=10)

ans1= StringVar()

#defining entry box ,where we enter or answer
e1=Entry(
    root,
    font=("verdana",16),
    textvariable=ans1,
)
e1.pack()

# creating a button which check the entered value
checkbutton=Button(
    root,
    text="Check",
    font=("Comic sans ms",16),
    width=16,
    bg="#2F363F",
    fg="#FFF222",
    relief= GROOVE,
    command=checkans,
)
checkbutton.pack(pady=30)

# creating a button which reset the label
resetbutton=Button(
    root,
    text="Reset",
    font=("Comic sans ms",16),
    width=16,
    bg="#2F363F",
    fg="#FFF222",
    relief= GROOVE,
    command=res,

)
resetbutton.pack()
# calling function and mainloop
working()
root.mainloop()
