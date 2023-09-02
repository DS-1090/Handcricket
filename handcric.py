import tkinter as tk
from tkinter import Label, Entry,Button
import tkinter.messagebox
import random
#from PIL import ImageTk, Image  

r = tk.Tk()

myscore=0
comscore=0
L = Label(r)
L.pack()

def myfirstbat():
    global myscore, comscore
    l7 = Label(text="\nEnter runs:",bg="#EEE0E5")
    l7.pack()
    p = Entry(r)
    p.pack()
    l=Label()
    l.pack()
    def func(z):
        global myscore, comscore
        
        e=int(p.get())
        if e in range(7):
                a= random.randint(0, 6)
                if a==e:
                    l.config(text=f"You are out,score={myscore}",bg="#EEE0E5")
                    p.config(state="disabled")
                    myball()
                else:
                    myscore = myscore+e
                    l.config(text=f"Run={e},score={myscore}",bg="#EEE0E5")
                    p.delete(0, 'end')

        else:
                  tkinter.messagebox.showinfo("Error", "enter val btw 0 to 6")
                  p.delete(0, 'end')

                
    p.bind("<Return>", func)
 
def myball():
  global myscore,comscore
  l = Label(r,text="\nEnter(to ball):",bg="#EEE0E5")
  l.pack()
  p = Entry(r)
  p.pack()
  m=Label()
  m.pack()
  def func(z):
    global myscore,comscore
    e = int(p.get())
    if(e>-1 and e<7):
        a=random.randint(0,6)
        if(a==e):
          #L.config(text=f"computer is out,you win,computer score={comscore}")
          tkinter.messagebox.showinfo("Result", f"You win!, computer score= {comscore+a} \n close window")
          p.config(state="disabled")

          
        if(comscore>myscore):
          #L.config(text="computer wins!")
          tkinter.messagebox.showinfo("Result", "Computer wins! \n close window")
          p.config(state="disabled")


        else:
          comscore+=a
          m.config(text=f"Run={a},Computer score={comscore}",bg="#EEE0E5")
          p.delete(0, 'end')

    else:
          tkinter.messagebox.showinfo("Error", "enter val btw 0 to 6")
          p.delete(0, 'end')
     
  
  p.bind("<Return>", func)

  


        
def myfirstball():
 
  global myscore,comscore
  L=Label()
  L.config(text="\nEnter(to ball):",bg="#EEE0E5")
  L.pack()
  p = Entry(r)
  m=Label()
  m.pack()
  p.pack()
  def func(z):
      global myscore,comscore
      j = p.get()
      e = int(j)
      
      if(e>-1 and e<7):
          a=random.randint(0,6)
          if(a==e):
            m.config(text=f"Computer is out, score={comscore}",bg="#EEE0E5")
            p.config(state="disabled")

            mybat()

          else:
            comscore=comscore+a
            m.config(text=f"Run={a},Computer score={comscore}",bg="#EEE0E5")
            p.delete(0, 'end')

      else:
                tkinter.messagebox.showinfo("Error", "Enter val btw 0 to 6")
                p.delete(0, 'end')           

      

          
  p.bind("<Return>", func)


def mybat():
    global myscore,comscore
    L.config(text="\nEnter runs:",bg="#EEE0E5")
    p = Entry(r)
    p.pack()
    m=Label()
    m.pack()
    def func(z):
      global myscore,comscore
      e = int(p.get())
      
      if(e>-1 and e<7):
          a=random.randint(0,6)
          if(a==e):
                   tkinter.messagebox.showinfo("Result", f"You win! {myscore+a} \n close window",bg="#EEE0E5")
                   p.config(state="disabled")

           
          if(comscore<myscore):
                   tkinter.messagebox.showinfo("Result", "You lost! \ close window",bg="#EEE0E5")
                   p.config(state="disabled")


          else:
            myscore=myscore+e
            m.config(text=f"run={e},my score={myscore}",bg="#EEE0E5")
            p.delete(0, 'end')

      else:
          tkinter.messagebox.showinfo("Error", "Enter val btw 0 to 6")
          p.delete(0, 'end')
       

      
    p.bind("<Return>", func)



def tosscoin():
    e1=e.get()
    l2=Label()
    l2.pack()
    a=random.randint(0,1)
    if((e1=="head" and a==0)or(e1=="tail" and a==1)):
        tkinter.messagebox.showinfo("Toss", "Yay! you won the toss")
        l2.config(text="\nchoose:",bg="#EEE0E5")
        l2.pack()
        bat=Button(r,text="Bat",command=myfirstbat,bg='teal')
        bat.pack()
        ball=Button(r,text="Ball",command=myfirstball,bg='teal')
        ball.pack()
    else:
        tkinter.messagebox.showinfo("Toss", "You lost the toss!")
        myfirstbat()
     
    
     





r.title("Hand Cricket")
r.geometry("600x600")
r.configure(bg="#EEE0E5")
l1 = Label(r, text="Enter 'head' or 'tail':",bg="#EEE0E5")  
l1.pack()
e = Entry(r)
e.pack()
b = tk.Button(r, text="Toss the Coin", font=("Arial", 10),command=tosscoin, bg='teal')
b.pack()



r.mainloop()
