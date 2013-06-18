from Tkinter import *

from time import *

import tkFont

SHOW_TOPBAR = True

def take():

    root = Toplevel()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(not SHOW_TOPBAR)
    root.geometry("%dx%d+0+0" % (w, h))


    root.title('New Note')

    font2 = tkFont.Font(family='Helvetica',size=20)

    f = Frame(root,width=500,height=500)

    f.grid()

    f.grid_propagate(0)

    Label(f,text='Enter the subject:').grid(row=1,column=0)

    a = Entry(f,width=15)

    a.grid(row=1,column=1)

    Label(f,text='Notes:(Standard HTML is accepted)').grid(row=2,column=0)

    b = Text(f,width=50,height=25)

    b.grid(row=3,column=0)

    dateNow = Label(root,text=strftime('%A %d %B %Y'),font=font2)

    timeNow = Label(root, text=strftime('%H:%M:%S'),font=font2)
    
    def update_time():
        
        timeNow['text'] = strftime('%H:%M:%S')
        dateNow['text'] = strftime('%A %d %B %Y')
        root.after(1000, update_time)

        
    root.after(1000, update_time)

    dateNow.grid(row=2,column=1)
    
    timeNow.grid(row=3, column=1)
    
    c = Button(f,text='Confirm',command=root.quit)

    c.grid(row=4,column=0)

    root.mainloop()

    subject = a.get()

    notes = b.get(1.0,END)

    root.destroy()

    return (subject,notes)

##Script level testing code.
##
##root = Tk()
##
##Label(root,text='See next window').pack()
##    
##add  = take()
##
##print add
##
##mainloop()
##
##root.destroy()
