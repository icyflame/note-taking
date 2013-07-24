from Tkinter import *

import tkMessageBox

alert = tkMessageBox.showinfo

import tkFont

import newNote

SUBJECT,NOTES = 0,1

SHOW_TOPBAR = True

fileName= 'notes.txt'

separator = '|'

class NoteTaking:

    def __init__(self):

        self.window = Tk()

        self.window.title('Notes')

        self.initFrameAndButtons()

        self.makeFullScreen()

    def makeFullScreen(self):

        root = self.window

        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(not SHOW_TOPBAR)
        root.geometry("%dx%d+0+0" % (w, h))

    def initFrame(self):

        try:

            self.frame.destroy()

        except:

            pass

        self.frame = Frame(self.window)

        self.frame.pack()

    def initFrameAndButtons(self):


        self.initFrame()

        listOfButtons = []

        self.big  = tkFont.Font(family='helvetica',size=24)

        listOfButtons.append(Button(self.frame,text='Add new',command=self.takeNewNote))
        listOfButtons.append(Button(self.frame,text='See old notes',command=self.seeOldNotes))
        listOfButtons.append(Button(self.frame,text='QUIT',command=self.quitwin,fg='black',bg='red'))

        
        for i in range(len(listOfButtons)):


            listOfButtons[i]['font']=self.big

            listOfButtons[i].pack(side='top')

    def takeNewNote(self):

        self.window.withdraw()

        a = newNote.take()

        self.subject = a[SUBJECT]

        self.notes = a[NOTES]

        isempty = True

        for x in a:

            if not x == '':

                isempty = False

                
        if isempty:

            alert('Empty','The note you entered is empty. We will not write it to file')

        else:

            self.write()

            alert('Note written','Note written to file')

        self.notes = ''

        self.subject = ''

        self.window.deiconify()

    def write(self):

        f = open(fileName,'a')

        import time       

        t = time.strftime("%A %d %B %Y %H:%M:%S")

        toBeWritten = '<span style="display:none">' + self.notes[:15] + '</span><br><h3>Time: </h3>' + t + '<br><h3>Subject: </h3>' + \
                        self.subject + '<h3><br>Notes:<br><br>' + self.notes + separator

        f.write(toBeWritten)

        f.close()

        print toBeWritten
        

    def seeOldNotes(self):

        records = []

        filin = open(fileName,'r')

        for i in filin:

            first = i.find(separator)

            second = i.find(separator,first+1)

            r = (i[:first-1],i[first+1:second],i[second+1:-1])

            for x in r:

                if not x == '':

                    records.append(r)

                    break

##        now records has all the records. and indexes of each tuple are so:
##
##            0: date and time
##            1: subject
##            2: notes
##

        counter = 1

        for i in records:

            if counter - 1 % 20 == 0:

                y = Toplevel()

                d = Frame(y)

                d.grid()

                Label(d,text='Serial').grid(row=0,column=0)
                Label(d,text='Time').grid(row=0,column=1)
                Label(d,text='Subject').grid(row=0,column=2)
                Label(d,text='Notes:').grid(row=0,column=3)


            Label(d,text=str(counter)).grid(row=counter,column=0)

            Label(d,text=i[0]).grid(row=counter,column=1)
            Label(d,text=i[1]).grid(row=counter,column=2)
            Label(d,text=i[2][:10] + '...').grid(row=counter,column=3)

            Button(d,text='See this record',command=self.SeeOneNote(i)).grid(row=counter,column=4)

            counter += 1


    def SeeOneNote(self,record):

        def showOneRec():

            toBeShown = '<br><h3>Time: </h3>' + record[0] + '<br><h3>Subject: </h3>' + \
                        record[1] + '<h3><br>Notes:<br><br>' + record[2]

            filout = open('1.html','w')

            filout.write(toBeShown)

            #alert('',toBeShown)

            filout.close()

            import webbrowser

            webbrowser.open('1.html')

            
        return showOneRec

    def quitwin(self):

        self.initFrame()

        self.frame.grid()

        self.frame.grid_propagate(1)

        self.big  = tkFont.Font(family='helvetica',size=24)

        r = self.frame

        c = 0

        import os

        try:

            os.remove('1.html')

        except:

            pass

        Label(r,text='Created by Siddharth Kannan',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Written on Python 2.7 and Tkinter 8.5',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='OS: LINUX MINT 14 NADIA',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='This software is licensed under the WTFPL license.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='See the copying file for more details.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Application will quit in 8 seconds.',font=self.big).grid(row=c,column=0)
        c+=1

        self.window.after(8000,self.window.destroy)



NoteTaking()

mainloop()       

##
##root = Tk()
##
##root.title('abcd')
##
##Label(root,text='this is a label').pack()
##
##mainloop()

