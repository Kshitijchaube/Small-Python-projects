from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("600x1000")
root.title("kc news")
f0 = Frame(root, width=800, height=70)
Label(f0, text="Latest Anime News", font="lucida 33 bold").pack()
Label(f0, text="September 9, 2099", font="lucida 13 bold").pack()
f0.pack()
texts=[]
photos=[]
for i in range(3):
    with open(f"texts/{i+1}.txt",mode='r') as f:
        a=f.read()
        b=''
        for j in range(len(a.split())):
            b+=a.split()[j] + ' '
            if j%6==0 and j!=0:
                b+='\n'
        texts.append(b)
    b=Image.open(f"images/{i+1}.jpg")
    b=b.resize((150,250))
    ph=ImageTk.PhotoImage(b)
    photos.append(ph)
for i in range(3):
    fi = Frame(root,width=400,height=100)
    l1=Label(fi,text=texts[i],font='Ariel 12',anchor='ne')
    if i % 2 == 0:
        l1.pack(side=LEFT)
    else:
        l1.pack(side=RIGHT)
    Label(fi,image=photos[i],anchor='e').pack()
    fi.pack(anchor='w')
root.mainloop()
