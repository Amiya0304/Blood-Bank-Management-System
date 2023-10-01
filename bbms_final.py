import tkinter as tk
from tkinter import ttk
import sqlite3 as sq
import btest as bt

con=sq.connect("Details.db")
c=con.cursor()

class main(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Blood Bank System")
        self.text1=tk.Text(self,height=10,width=45)
        self.photo = tk.PhotoImage(file='mainpg.png')
        self.text1.insert(tk.END, '\n')
        self.text1.image_create(tk.END, image=self.photo)
        self.text1.grid(row=4, column=7)
        self.b1=tk.Button(self,text='Donor',command=self.register)
        self.b1.grid(row=9,column=7)
        self.b2=tk.Button(self,text='Receiver',command=self.get)
        self.b2.grid(row=11,column=7)
        self.b3=tk.Button(self,text='Blood compatibility test',command=bt.display)
        self.b3.grid(row=13,column=7)
    def close(self):
        self.destroy()
        quit()
    def conf(self):
        self.rname=self.name1.get()
        self.g=self.radioval.get()
        print(self.g)
        self.rgender='F'
        if self.g==1:
            self.rgender="F"
        elif self.g==2:
            slef.rgender="M"
        self.dob1=self.day.get()
        self.dob2=self.month.get()
        self.dob3=self.year.get()
        self.rdob=str(self.dob1+"-"+self.dob2[:3]+"-"+self.dob3)
        self.rbgp=str(self.blood_group1.get())
        self.rcont=self.phone1.get()
        self.raddr=str(self.address1.get())
        slef.i=0
        self.li=c.execute('SELECT * FROM REG')
        for row in self.li:
            self.i=row[0]
        self.i+=1
        self.info=(self.i,self.rgender,self.rname,self.rbgp,self.rcont,self,raddr,self.rdob)
        self.inserting=c.execute('INSERT INTO REG VALUES(?,?,?,?,?,?,?)',self.info)
        con.commit()

        self.win2=tk.Tk()
        self.win2.title("Registration successfull")
        self.text=tk.Text(self.win2)
        text1='Your information has been inserted. Kindly note down your donor id '+str(self.i)
        self.text.insert(tk.END,text1)
        self.b1=tk.Button(self.win2,text='Exit',command=self.close)
        self.text.grid(row=1,column=2)
        self.b1.grid(row=2,colum=2)
        self.win2.mainloop()

    def register(self):
        self.years=[]
        for i in range(2022,1950,-1):
            self.years.append(i)
        self.days=[]
        for i in range(1,32):
            self.days.append(i)
        self.win=tk.Tk()
        self.win.tittle("Donor Registration")
        self.name=tl.Label(self.win,text='Name:')
        self.gen=tk.Label(self.win,text='Gender:')
        self.dob=tk.Label(self.win,text='Date of Birth:')
        self.radioval=tk.IntVar()
        self.r1=tk.Radiobutton(self.win,text="Female",variable=self.radioval,value=1)
        self.r2=tk.Radiobutton(self.win,text="Male",variable=self.radioval,value=2)
        self.bgp=tk.Label(self.win,text="Blood Groupp:")
        self.phone=tk.Label(self.win,text='Contact NO.:')
        self.address=tk.Label(self.win,text='Address:')

        self.name1=tk.StringVar()
        self.name1=tk.Entry(self.win)
        self.phone1=tk.Entry(self.win)
        self.address1=tk.Entry(self.win)
        self.blood_group1=ttl.Combobox(self.win,value=['A+','A-','B+','B-','AB+','AB-','O+','O-'])
        self.day=ttk.Combobox(self.win,values=self.days)
        self.month=ttk.Combobox(self.win,values=['January','Feburary','March','April','May','June','July','August','september','October','November','December'])
        self.year=ttk.Combobox(self.win,values=self.years)
        self.day.current()
        self.month.current()
        self.year.current()
        self.bloodblood_group1.current()
        self.sub=tk.Button(self.win,text='Submit',command=self.conf)
        self.name.grid(row=1,column=1)
        self.gen.grid(row=2,column=2,columnspan=2)
        self.r1.grid(row=2,column=1)
        self.r2.grid(row=2,column=3)
        self.dob.grid(row=3,column=1)
        self.day.grid(row=3,column=2)
        self.month.grid(row=3,column=2)
        self.year.grid(row=3,column=4)
        self.bgp.grid(row=4,column=1)
        self.blood_group1.grid(row=4,column=2)
        self.phone.grid(row=5,column=1)
        self.phone1.grid(row=5,column=2)
        self.address.grid(row=6,column=1)
        self.address1.grid(row=6,column=2)
        self.sub.grid(row=10,column=2,columspan=2)
        self.win.mainloop()

    def print_data(self):
        self.recv_bg=self.e2.get()
        self.recv_city=self.e3.get()
        self.printing=c.execute('SELECT ID,NAME,GENDER,BLOODGROUP,PHONE,CITY,DOB FROM REG R JOIN COMPAT C WHERE C.RBGRP=? AND R.BLOODGROUP=C.DBGRP AND CITY=?;',(self,recv_bg,self.recv_city,))
        count=0
        row1=()
        for row in self.printing:
             row1+=row
             count+=1
        if count==0:
             self.C=tk.Tk()
             self.C.title("Donor Details")
             tk.Label(self.C,text="Sorry! Required donor could not be found in your city").grid(row=0,column=0)
             self.c1.tk.Button(self.C,text="Exit",command=self.close)
             self.c1.grid(row=1,column=0)
             self.C.mainloop()
        else:
             self.C.tk.Tk()
             self.C.title('Donor Deatils')
             tk.Label(self.C,text='ID').grid(row=0,column=0)
             tk.Label(self.C,text="Gender").grid(row=0,column=1)
             tk.Label(self.C,text="Nmae").grid(rpw=0,column=2)
             tk.Label(self.C,text="Blood Group",).grid(row=0,column=3)
             tk.Label(self.C,text="Phone Number").grid(row=0,column=4)
             tk.Label(self.C,text="City").grid(row=0,column=5)
             tk.Label(self.C,text="DOB").grid(row=0,column=6)
             self.c1=tk.Button(self.c,text="Exit",command=self.close)
             k=0
             for i in range(1,count+1):
                 tk.Label(self.C,text=row[i+k-1]).grid(row=i,column=0)
                 tk.Label(self.C,text=row[i+k+1-1]).grid(row=i,column=1)
                 tk.Label(self.C,text=row[i+k+2-1]).grid(row=i,column=2)
                 tk.Label(self.C,text=row[i+k+3-1]).grid(row=i,column=3)
                 tk.Label(self.C,text=row[i+k+4-1]).grid(row=i,column=4)
                 tk.Label(self.C,text=row[i+k+5-1]).grid(row=i,column=5)
                 tk.Label(self.C,text=row[i+k+6-1]).grid(row=i,column=6)
                 k+=6
             self.c1.grid(row=count+1,column=2,columnspan=3)
             self.C.mainloop()

    def get(self):
        self.B=tk.Tk()
        self.B.title("Recipient page")
        tk.Label(self.B,text="recipient blood group:").grid(row=0)
        tk.Label(self.B,text="Recipient City:").grid(row=1)
        self.e3=tk.Entry(self.B)
        self.e2==ttk.Combobox(Self.B,values=["A+","A-","B+","B-","O+","O-","AB+","AB-"])
        self.b1=tk.Button(self.b,text="Go",command=self.print)
        self.e2.grid(row=0,column=1)
        self.e3.grid(row=1,column=1)
        self.b1.grid(row=3,column=1,columnspan=2)
        self.B.mainloop()
if __name__=='main':
    main.mainloop()
         

            
