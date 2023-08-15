from tkinter import *
from PIL import ImageTk, Image
import re
global w1,w2,w3,w7
import pymysql

db=pymysql.Connect(host="localhost",user="root",password="Kalpana@2004",database="Mini_Project")
cur=db.cursor()
w1=Tk()
w1.title("SIGN-UP PAGE")
w1.geometry('1366x768')
c = Canvas(w1, width=1366, height=768, bg='white')
c.pack()
img = ImageTk.PhotoImage(Image.open("bg1.jpg")) 
c.create_image(0,0,anchor=NW, image=img)

        
def Login():
    global a,b,c,d,e
    a=w1e1.get()
    b=w1e2.get()
    c=w1e3.get()
    d=w1e4.get()
    e=w1e5.get()

    query="insert into signupdetails values(%s,%s,%s,%s,%s)"
    val=[a,b,c,d,e]
    cur.execute(query,val)
    db.commit()
    if a.isalpha():
        if b.isnumeric():
            c=re.findall("[0-9]",c)
            if len(c)==10:
                if ("@" and "@gmail.com") in d:
                    if len(e)>=8:
                        w2=Toplevel(w1)
                        w2.geometry("1366x768")
                        load=Image.open("D:\\Cloth Ordering Project\\bg2.jpg")
                        photo=ImageTk.PhotoImage(load)
                        label=Label(w2,image=photo)
                        label.image=photo
                        label.place(x=0,y=0)
                        w2.title("Log-In Page")
                        
                        w2ll=Label(w2,text="LOG-IN PAGE",font="calibri 25 bold underline",fg="Darkblue",bg="lightyellow").place(x=500,y=20)
                        w2l2=Label(w2,text="E-Mail ID:",font="Arial 10 bold",bg="lightyellow").place(x=440,y=100)
                        w2e1=Entry(w2,width=30)
                        w2e1.place(x=600,y=100)
                        w2l3=Label(w2,text="Password:",font="Arial 10 bold",bg="lightyellow").place(x=440,y=150)
                        w2e2=Entry(w2,width=30)
                        w2e2.place(x=600,y=150)
                        
                        def check():
                            global f,g
                            f=w2e1.get()
                            g=w2e2.get()
                            
                            if d==f:
                                if e==g:
                                    def men():
                                        w4=Toplevel(w1)
                                        w4.geometry("1366x768")
                                        load=Image.open("D:\\Cloth Ordering Project\\Mens\\bg.jpg")
                                        photo=ImageTk.PhotoImage(load)
                                        label=Label(w4,image=photo)
                                        label.image=photo
                                        label.place(x=0,y=0)
                                        w4.title("MEN'S PAGE")
                                        
                                        w4l1=Label(w4,text="SHIRTS",font="Cambria 18 bold").place(x=680,y=10)

                                        f1 = Frame(w4, width=100, height=150)
                                        f1.pack()
                                        f1.place(x=80,y=70)
                                        img1 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Camp Flannel Shirt 1.jpg"))
                                        l = Label(f1, image = img1).pack()
                                        Checkbutton(w4,text="Camp Flannel Shirt \n Rs.450",command=lambda:kart(1,450)).place(x=80,y=300)

                                        f2 = Frame(w4, width=100, height=150)
                                        f2.pack()
                                        f2.place(x=330,y=70)
                                        img2 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Sleeve Flannel Shirt 2.jpg"))
                                        l = Label(f2, image = img2).pack()
                                        Checkbutton(w4,text="Sleeve Flannel Shirt \n Rs.550",command=lambda:kart(1,550)).place(x=330,y=300)

                                        f3 = Frame(w4, width=100, height=150)
                                        f3.pack()
                                        f3.place(x=580,y=70)
                                        img3 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Casual Poplin Shirt 3.jpg"))
                                        l = Label(f3, image = img3).pack()
                                        Checkbutton(w4,text="Casual Poplin Shirt \n Rs.650",command=lambda:kart(1,650)).place(x=550,y=300)

                                        f4 = Frame(w4, width=100, height=150)
                                        f4.pack()
                                        f4.place(x=830,y=70)
                                        img4 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Button Down Shirt 4.jpg"))
                                        l = Label(f4, image = img4).pack()
                                        Checkbutton(w4,text="Button Down Shirt \n Rs.750",command=lambda:kart(1,750)).place(x=800,y=300)

                                        f5 = Frame(w4, width=100, height=150)
                                        f5.pack()
                                        f5.place(x=1080,y=70)
                                        img5 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Comfort Flex Shirt 5.jpg"))
                                        l = Label(f5, image = img5).pack()
                                        Checkbutton(w4,text="Comfort Flex Shirt \n Rs.850",command=lambda:kart(1,850)).place(x=1080,y=300)

                                        f6 = Frame(w4, width=100, height=150)
                                        f6.pack()
                                        f6.place(x=80,y=400)
                                        img6 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Dri-Power T-Shirt 6.jpg"))
                                        l = Label(f6, image = img6).pack()
                                        Checkbutton(w4,text="Dri-Power T-Shirt \n Rs.950",command=lambda:kart(1,950)).place(x=70,y=600)

                                        f7 = Frame(w4, width=100, height=150)
                                        f7.pack()
                                        f7.place(x=330,y=400)
                                        img7 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Long Sleeve T-Shirt 7.jpg"))
                                        l = Label(f7, image = img7).pack()
                                        Checkbutton(w4,text="Long Sleeve T-Shirt \n Rs.1000",command=lambda:kart(1,1000)).place(x=320,y=600)

                                        f8 = Frame(w4, width=100, height=150)
                                        f8.pack()
                                        f8.place(x=580,y=400)
                                        img8 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Essential T-Shirt 8.jpg"))
                                        l = Label(f8, image = img8).pack()
                                        Checkbutton(w4,text="Essential T-Shirt \n Rs.1100",command=lambda:kart(1,1100)).place(x=570,y=600)

                                        f9 = Frame(w4, width=100, height=150)
                                        f9.pack()
                                        f9.place(x=830,y=400)
                                        img9 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Thermal Shirt 9.jpg"))
                                        l = Label(f9, image = img9).pack()
                                        Checkbutton(w4,text="Thermal Shirt \n Rs.1110",command=lambda:kart(1,1110)).place(x=820,y=600)

                                        f10 = Frame(w4, width=100, height=150)
                                        f10.pack()
                                        f10.place(x=1080,y=400)
                                        img10 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Mens\Crew Neck T-Shirt 10.jpg"))
                                        l = Label(f10, image = img10).pack()
                                        Checkbutton(w4,text="Crew Neck T-Shirt \n Rs.780",command=lambda:kart(1,780)).place(x=1070,y=600)

                                        w4b1=Button(w4,text="Back",fg='white',bg='red',height=1,width=6,command=w4.destroy).place(x=10,y=15)
                                        w4b2=Button(w4,text="Finish",fg='white',bg='green',height=1,width=6,command=confirm).place(x=1100,y=15)
                                        w4.mainloop()
                                    def women():
                                        w5=Toplevel(w1)
                                        w5.geometry("1366x768")
                                        load=Image.open("D:\\Cloth Ordering Project\\women\\bg.jpg")
                                        photo=ImageTk.PhotoImage(load)
                                        label=Label(w5,image=photo)
                                        label.image=photo
                                        label.place(x=0,y=0)
                                        w5.title("WOMEN'S PAGE")
                                        w5l1=Label(w5,text="SAREES",font="Cambria 18 bold").place(x=680,y=10)
                                        
                                        f11 = Frame(w5, width=100, height=150)
                                        f11.pack()
                                        f11.place(x=80,y=70)
                                        img11 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Banarasi silks 100x150.jpg"))
                                        l = Label(f11, image = img11).pack()
                                        Checkbutton(w5,text="Banarasi silks \n Rs.800",command=lambda:kart(1,800)).place(x=80,y=300)

                                        f2 = Frame(w5, width=100, height=150)
                                        f2.pack()
                                        f2.place(x=330,y=70)
                                        img2 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Yellow Georgette Saree 2.jpg"))
                                        l = Label(f2, image = img2).pack()
                                        Checkbutton(w5,text="Georgette Saree \n Rs.750",command=lambda:kart(1,750)).place(x=330,y=300)

                                        f3 = Frame(w5, width=100, height=150)
                                        f3.pack()
                                        f3.place(x=580,y=70)
                                        img3 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Indian Style Fancy Saree 3.jpg"))
                                        l = Label(f3, image = img3).pack()
                                        Checkbutton(w5,text="Fancy Saree \n Rs.900",command=lambda:kart(1,900)).place(x=580,y=300)

                                        f4 = Frame(w5, width=100, height=150)
                                        f4.pack()
                                        f4.place(x=830,y=70)
                                        img4 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Lichi Silk Party wear Saree 4.jpg"))
                                        l = Label(f4, image = img4).pack()
                                        Checkbutton(w5,text="Party wear Saree \n Rs.1000",command=lambda:kart(1,1000)).place(x=830,y=300)

                                        f5 = Frame(w5, width=100, height=150)
                                        f5.pack()
                                        f5.place(x=1080,y=70)
                                        img5 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Pedding Embroidery work Saree 5.jpg"))
                                        l = Label(f5, image = img5).pack()
                                        Checkbutton(w5,text="Embroidery work Saree \n Rs.600",command=lambda:kart(1,600)).place(x=1080,y=300)

                                        f6 = Frame(w5, width=100, height=150)
                                        f6.pack()
                                        f6.place(x=80,y=400)
                                        img6 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Salwar Kameez Suit 6.jpg"))
                                        l = Label(f6, image = img6).pack()
                                        Checkbutton(w5,text="Salwar Kameez Suit \n Rs.550",command=lambda:kart(1,550)).place(x=80,y=600)

                                        f7 = Frame(w5, width=100, height=150)
                                        f7.pack()
                                        f7.place(x=330,y=400)
                                        img7 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Ghaghra Style Salwar Kameez 7.jpg"))
                                        l = Label(f7, image = img7).pack()
                                        Checkbutton(w5,text="Ghaghra Style Salwar Kameez \n Rs.950",command=lambda:kart(1,950)).place(x=330,y=600)

                                        f8 = Frame(w5, width=100, height=150)
                                        f8.pack()
                                        f8.place(x=580,y=400)
                                        img8 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Anarkali kurta 8.jpg"))
                                        l = Label(f8, image = img8).pack()
                                        Checkbutton(w5,text="Anarkali kurta \n Rs.1100",command=lambda:kart(1,1100)).place(x=580,y=600)

                                        f9 = Frame(w5, width=100, height=150)
                                        f9.pack()
                                        f9.place(x=830,y=380)
                                        img9 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Kurta Pant with Dupatta Set 9.jpg"))
                                        l = Label(f9, image = img9).pack()
                                        Checkbutton(w5,text="Kurta Pant with Dupatta Set \n Rs.890",command=lambda:kart(1,890)).place(x=830,y=600)

                                        f10 = Frame(w5, width=100, height=150)
                                        f10.pack()
                                        f10.place(x=1080,y=400)
                                        img10 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\women\Wedding Wear Designer 10.jpg"))
                                        l = Label(f10, image = img10).pack()
                                        Checkbutton(w5,text="Wedding Wear Designer \n Rs.1200",command=lambda:kart(1,1200)).place(x=1080,y=600)

                                        w4b1=Button(w5,text="Back",fg='white',bg='red',height=1,width=6,command=w5.destroy).place(x=10,y=15)
                                        w4b2=Button(w5,text="Finish",fg='white',bg='green',height=1,width=6,command=confirm).place(x=1100,y=15)

                                        w5.mainloop()

                                    def kids():
                                        w6=Toplevel(w1)
                                        w6.geometry("1366x768")
                                        load=Image.open("D:\\Cloth Ordering Project\\Kids\\bg.jpg")
                                        photo=ImageTk.PhotoImage(load)
                                        label=Label(w6,image=photo)
                                        label.image=photo
                                        label.place(x=0,y=0)
                                        w6.title("KID'S PAGE")
                                        w6l1=Label(w6,text="KIDS",font="Cambria 18 bold underline").place(x=680,y=10)

                                        f1 = Frame(w6, width=100, height=150)
                                        f1.pack()
                                        f1.place(x=80,y=70)
                                        img1 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Stain Short Sleeve 1.jpg"))
                                        l = Label(f1, image = img1).pack()
                                        Checkbutton(w6,text="Stain Short Sleeve \n Rs.400",command=lambda:kart(1,400)).place(x=80,y=300)

                                        f2 = Frame(w6, width=100, height=150)
                                        f2.pack()
                                        f2.place(x=330,y=70)
                                        img2 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Tech Short Sleeve 2.jpg"))
                                        l = Label(f2, image = img2).pack()
                                        Checkbutton(w6,text="Tech Short Sleeve \n Rs.500",command=lambda:kart(1,500)).place(x=330,y=300)

                                        f3 = Frame(w6, width=100, height=150)
                                        f3.pack()
                                        f3.place(x=580,y=70)
                                        img3 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Heavy Cotton T-Shirt 3.jpg"))
                                        l = Label(f3, image = img3).pack()
                                        Checkbutton(w6,text="Heavy Cotton T-Shirt \n Rs.550",command=lambda:kart(1,550)).place(x=580,y=300)

                                        f4 = Frame(w6, width=100, height=150)
                                        f4.pack()
                                        f4.place(x=830,y=70)
                                        img4 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Tagless T-Shirt 4.jpg"))
                                        l = Label(f4, image = img4).pack()
                                        Checkbutton(w6,text="Tagless T-Shirt \n Rs.490",command=lambda:kart(1,490)).place(x=830,y=300)

                                        f5 = Frame(w6, width=100, height=150)
                                        f5.pack()
                                        f5.place(x=1080,y=70)
                                        img5 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Short Sleeve T-Shirt 5.jpg"))
                                        l = Label(f5, image = img5).pack()
                                        Checkbutton(w6,text="Short Sleeve T-Shirt \n Rs.470",command=lambda:kart(1,470)).place(x=1080,y=300)

                                        f6 = Frame(w6, width=100, height=150)
                                        f6.pack()
                                        f6.place(x=80,y=400)
                                        img6 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Girls Casual Tunic Tops 6.jpg"))
                                        l = Label(f6, image = img6).pack()
                                        Checkbutton(w6,text="Girls Casual Tunic Tops \n Rs.600",command=lambda:kart(1,600)).place(x=80,y=600)

                                        f7 = Frame(w6, width=100, height=150)
                                        f7.pack()
                                        f7.place(x=330,y=400)
                                        img7 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Girls Long T-Shirt 7.jpg"))
                                        l = Label(f7, image = img7).pack()
                                        Checkbutton(w6,text="Girls Long T-Shirt \n Rs.700",command=lambda:kart(1,700)).place(x=330,y=600)

                                        f8 = Frame(w6, width=100, height=150)
                                        f8.pack()
                                        f8.place(x=580,y=400)
                                        img8 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Girls Striped Short Sleeve 8.jpg"))
                                        l = Label(f8, image = img8).pack()
                                        Checkbutton(w6,text="Girls Striped Short Sleeve \n Rs.490",command=lambda:kart(1,490)).place(x=580,y=600)

                                        f9 = Frame(w6, width=100, height=150)
                                        f9.pack()
                                        f9.place(x=830,y=400)
                                        img9 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Girls Supersoft Tech 9.jpg"))
                                        l = Label(f9, image = img9).pack()
                                        Checkbutton(w6,text="Girls Supersoft Tech \n Rs.680",command=lambda:kart(1,680)).place(x=830,y=600)

                                        f10 = Frame(w6, width=100, height=150)
                                        f10.pack()
                                        f10.place(x=1080,y=400)
                                        img10 = ImageTk.PhotoImage(Image.open("D:\Cloth Ordering Project\Kids\Girls Casual Long Sleeve 10.jpg"))
                                        l = Label(f10, image = img10).pack()
                                        Checkbutton(w6,text="Girls Casual Long Sleeve \n Rs.900",command=lambda:kart(1,900)).place(x=1080,y=600)

                                        w4b1=Button(w6,text="Back",fg='white',bg='red',height=1,width=6,command=w6.destroy).place(x=10,y=15)
                                        w4b2=Button(w6,text="Finish",fg='white',bg='green',height=1,width=6,command=confirm).place(x=1100,y=15)

                                        w6.mainloop()
                                    def menu():
                                        w3=Toplevel(w1)
                                        w3.geometry("1366x768")
                                        load=Image.open("D:\\Cloth Ordering Project\\bg3.jpg")
                                        photo=ImageTk.PhotoImage(load)
                                        label=Label(w3,image=photo)
                                        label.image=photo
                                        label.place(x=0,y=0)
                                        w3.title("MAIN MENU PAGE")
                                        w3l1=Label(w3,text="WELCOME "+ a +" KINDLY SELECT OPTION",font="Calibri 25 bold ",fg="Dark blue").pack()
                                        w3b1=Button(w3,text="MEN",height=3,width=12,command=men).place(x=600,y=200)
                                        w3b2=Button(w3,text="WOMEN",height=3,width=12,command=women).place(x=600,y=350)
                                        w2b3=Button(w3,text="KIDS",height=3,width=12,command=kids).place(x=600,y=500)
                                        w2b4=Button(w3,text="Cancel",fg='white',bg='red',height=1,width=6,command=w3.destroy).place(x=100,y=600)
                                        w3.mainloop()
                                    menu()
                                else:
                                    w2l5=Label(w2,text="(Incorrect E-Mail Id.!)",font="ariel 7 bold",fg="red").place(x=600,y=120)
                            else:
                                w2l4=Label(w2,text="(Incorrect Password.Kindly Check!)",font="ariel 7 bold",fg="red").place(x=600,y=170)
                                    
                        w2b3=Button(w2,text="Cancel",width=10,height=2,command=w2.destroy).place(x=500,y=220)
                        w2b4=Button(w2,text="LOG-IN",width=10,height=2,command=check).place(x=700,y=220)

                    else:
                        w1l11=Label(w1,text="(Password must have minimum 8 characters!)",font="ariel 7 bold",fg="red").place(x=600,y=280)
                else:
                    w1l10=Label(w1,text="(Invalid E-Mail ID)",font="ariel 7 bold",fg="red").place(x=600,y=240)
            else:
                w1l9=Label(w1,text="Kindly enter correct mobile number!",font="ariel 7 bold",fg="red").place(x=600,y=200)
        else:
            w1l8=Label(w1,text="Kindly enter Valid Age!",font="ariel 7 bold",fg="red").place(x=600,y=160)
    else:
        w1l7=Label(w1,text="Enter Valid name!",font="ariel 7 bold",fg="red").place(x=600,y=120)

    
w1l1=Label(w1,text="SIGN - UP PAGE",font="calibri 25 bold underline",fg="darkblue").place(x=500,y=20)

w1l2=Label(w1,text="Name:",font="Arial 13 bold").place(x=440,y=100)
w1e1=Entry(w1,width=30)
w1e1.place(x=600,y=100)

w1l3=Label(w1,text="Age:",font="Arial 13 bold").place(x=440,y=140)
w1e2=Entry(w1,width=30)
w1e2.place(x=600,y=140)

w1l4=Label(w1,text="Contact Number:",font="Arial 13 bold").place(x=440,y=180)
w1e3=Entry(w1,width=30)
w1e3.place(x=600,y=180)

w1l5=Label(w1,text="E-Mail ID:",font="Arial 13 bold").place(x=440,y=220)
w1e4=Entry(w1,width=30)
w1e4.place(x=600,y=220)

w1l6=Label(w1,text="Password:",font="Arial 13 bold").place(x=440,y=260)
w1e5=Entry(w1,width=30)
w1e5.place(x=600,y=260)



w1b1=Button(w1,text="Cancel",width=10,height=2,command=w1.destroy).place(x=450,y=320)
w1b2=Button(w1,text="SIGN-UP",width=10,height=2,command=Login).place(x=690,y=320)

k=[]
def kart(o,r):
    global y
    if o==1:
        k.append(r)
        print(k)
    y=sum(k)
    print("Your Total Amount is:",y)
                   
def confirm():
    w7=Toplevel(w1)
    w7.geometry("1366x768")
    load=Image.open("D:\Cloth Ordering Project\confirm page bg.jpg")
    photo=ImageTk.PhotoImage(load)
    label=Label(w7,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    w7.title("CONFIRMATION PAGE")
    w7l1=Label(w7,text="Thank you for \n Visiting Us!",font="Arial 25 bold underline",fg="brown").place(x=850,y=100)
    w7l2=Label(w7,text="Your Total Amount is: "+str(y),font="Arial 20 bold").place(x=850,y=300)

    def payment():
        w8=Toplevel(w1)
        w8.geometry("1366x768")
        load=Image.open("D:\Cloth Ordering Project\payment page bg.jpg")
        photo=ImageTk.PhotoImage(load)
        label=Label(w8,image=photo)
        label.image=photo
        label.place(x=0,y=0)
                      
        w8spl=Label(w8,text="You have to pay : "+str(y),font="timesnewroman 10",fg="red").place(x=800,y=320)
        w8l1=Label(w8,text="Select mode of payment:",font="Calibri 30 bold",fg="brown").place(x=800,y=100)

        def check(op):
            if op==1:
                w8l2=Label(w8,text="Enter an Amount:",font="Calibri 15 bold",fg="brown").place(x=800,y=450)
                w8e1=Entry(w8,width=10)
                w8e1.place(x=800,y=500)
                def GPcheck():
                    w8l4=Label(w8,text="Amount Successfully received through GPay").place(x=800,y=550)
                GpB=Button(w8,height=1,width=10,text="PAY",fg="skyblue",command=GPcheck).place(x=800,y=590)
                w8b2=Button(w8,text="LOGOUT",fg='white',bg='red',height=1,width=6,command=w1.destroy).place(x=1100,y=15)
                                    
            if op==2:
                w8l2=Label(w8,text="Enter an Amount:",font="Calibri 15 bold",fg="brown").place(x=800,y=450)
                w8e1=Entry(w8,width=10)
                w8e1.place(x=800,y=500)
                def PPcheck():
                    w8l5=Label(w8,text="Amount Successfully received through PhonePe").place(x=800,y=550)
                GpB=Button(w8,height=1,width=10,text="PAY",fg="violet",command=PPcheck).place(x=800,y=590)
                w8b2=Button(w8,text="LOGOUT",fg='white',bg='red',height=1,width=6,command=w1.destroy).place(x=1100,y=15)
                                    
            if op==3:
                w8l2=Label(w8,text="Enter an Amount:",font="Calibri 15 bold",fg="brown").place(x=800,y=450)
                w8e1=Entry(w8,width=10)
                w8e1.place(x=800,y=500)
                def PMcheck():
                    w8l6=Label(w8,text="Amount Successfully received through Paytm").place(x=800,y=550)
                GpB=Button(w8,height=1,width=10,text="PAY",fg="red",command=PMcheck).place(x=800,y=590)
                w8b2=Button(w8,text="LOGOUT",fg='white',bg='red',height=1,width=6,command=w1.destroy).place(x=1100,y=15)
                      
        o1=Checkbutton(w8,text="Google Pay",command=lambda:check(1)).place(x=800,y=160)
        o2=Checkbutton(w8,text="PhonePe",command=lambda:check(2)).place(x=800,y=220)
        o3=Checkbutton(w8,text="Paytm",command=lambda:check(3)).place(x=800,y=280)
                            
    w7b1=Button(w7,text="PAYMENT",height=2,width=8,bg="yellow",fg="black",command=payment).place(x=850,y=500)
                        
                     
