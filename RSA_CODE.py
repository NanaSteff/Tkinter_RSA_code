#!/usr/bin/env python
# coding: utf-8

# In[45]:


from tkinter import Tk, Entry, Label, IntVar,ALL, Button, LabelFrame, W

def Bezout_coeff(a,b):
    u,v,x,y=1,0,0,1
    while b%a!=0:
        quo=b//a
        x,y,u,v=u-x*quo,v-y*quo,x,y
        b,a=a,b%a
    return a,y,x
    
    
def entry3_listen(*args):
    p=int(ent1.get())
    q=int(ent2.get())
    e=int(ent3.get())
    n=p*q
    phi_n=(p-1)*(q-1)
    g,d,x = Bezout_coeff(e,phi_n)
    if g!=1:
        ent3.configure(bg='red')
        chaine.configure(text = "Wrong choice",fg='red')
    else:
        d=d%phi_n
        ent3.configure(bg='white')
        chaine.configure(text = "Your private key is {}".format(d),fg='purple')
    
    

def cipher(*args):
    m=int(ent4.get())
    p=int(ent1.get())
    q=int(ent2.get())
    e=int(ent3.get())
    n=p*q    
    m=(m**e)%n
    chn1.configure(text="Ciphertext is {}".format(m),fg='purple')    

    
def focusent2(*args):
    ent2.focus()
    

def focusent3(*args):
    ent3.focus()

fen=Tk()
indication=Label(fen,bg='MistyRose3',text='Enter your first prime number choice in the p case and\n\
your second prime number choice in the q case. After that, Make your choice of\n\
public key which is coprime to (p-1)(q-1)')
indication.grid(row=0,column=0,columnspan=2)


fr1=LabelFrame(fen,text="Key setting")
txt1 = Label(fr1, text = 'p',bg='MistyRose')
txt2 = Label(fr1, text = 'q',bg='MistyRose')
txt3 = Label(fr1, text = 'e',bg='MistyRose')

txt1.grid(row =0,column=0,sticky=W)
txt2.grid(row =1,column=0,sticky=W)
txt3.grid(row =2,column=0,sticky=W)

bou1=Button(fr1,text="Get your key!!",bg="purple",fg='white',command=entry3_listen)
bou1.grid(row=3,column=0,columnspan=2)
fr1.grid(row=1,column=0)


ent1=Entry(fr1)
ent1.grid(row =0, column=1)
ent2=Entry(fr1)

ent2.grid(row =1, column=1)
ent3=Entry(fr1)
ent3.grid(row =2, column=1)

ent1.bind("<Return>",focusent2)
ent2.bind("<Return>",focusent3)
ent3.bind("<Return>")
chaine=Label(fr1)
chaine.grid(row=4,column=1)



fr2=LabelFrame(fen,text="Message")
fr2.grid(row=1,column=1)
txt4 = Label(fr2, text = 'Enter your message',bg='MistyRose')
txt4.grid(row =0,padx =5, pady =20)
ent4=Entry(fr2)
ent4.grid(row =1, column=0)
bout1=Button(fr2,text='Get encrypted message',bg="purple",fg='white',command=cipher)
bout1.grid(row=2,column=0)
chn1=Label(fr2)
chn1.grid(row=3,column=0)
fen.mainloop()


# In[ ]:




