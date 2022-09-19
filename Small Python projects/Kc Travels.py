from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("500x300")
def gigity():
    with open("Kc_travelform",mode='a') as f:
        f.write(f"Name:{name_val.get()}\nAge:{age_val.get()}\nGender:{gender_val.get()}\nInsurance:{insurance_var.get()}\nfood:{food_var.get()}\nAc coach:{ac_var.get()}\n\n\n")
    tmsg.showinfo('Thank you','Thanks you Registering')
    print('Thanks for registering')
    exit()
Label(root,text='Welcome to Kc Travels',font='comicsansms 12 bold',pady=15).grid(row=0,column=3)
Label(root,text='Name:').grid(row=1,column=2)
Label(root,text='Age:').grid(row=2,column=2)
Label(root,text='Gender:').grid(row=3,column=2)

#Entry variables
name_val=StringVar()
age_val=StringVar()
gender_val=StringVar()
ac_var=IntVar()
insurance_var=IntVar()
food_var=IntVar()
#insurance_var.set(1)
#Entry Labels
Entry(root,textvariable=name_val).grid(row=1,column=3)
Entry(root,textvariable=age_val).grid(row=2,column=3)
Entry(root,textvariable=gender_val).grid(row=3,column=3)
#checkbox
Checkbutton(text='Want to opt for Ac coach',variable=ac_var).grid(row=6,column=3)
Checkbutton(text='Want to prebook your meals',variable=food_var).grid(row=7,column=3)
#RadioButton
Label(root,text='Want to opt for Travel Insurance').grid(row=4,column=2)
radio=Radiobutton(text='Yes',variable=insurance_var,value=1).grid(row=4,column=3)
radio=Radiobutton(text='No',variable=insurance_var,value=0).grid(row=4,column=4)

#button
Button(root,text='Submit Details to Kc Travels',command=gigity).grid(row=8,column=3)
root.mainloop()
