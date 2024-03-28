import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#from PIL import Image,ImageTk


def Laptop_Showroom():
    username = entry_username.get()
    password = entry_password.get()
    
    if  username=="lap"  and  password=="123" :
        messagebox.showinfo("Logged","Login Sucessfully")
        open() 
    elif  not username != "lap" or not password !="123":
      messagebox.showerror("Error","placed the correct username and password!")
    else:
     messagebox.showerror("Error", "Both username and password must be filled!")
def open():   
    a=tk.Tk()
  #Company Details
    tk.Label(a, text="Stark Dell", fg="blue", font=("TimesNewRoman", 25)).place(x=650,y=5)
    tk.Label(a, text="P.R TOWERS,Kottai Road", fg="black", font=("Times New Roman", 14)).place(x=620,y=50)
    tk.Label(a, text="opposite to Ulavar santhai ", fg="black", font=("Times New Roman", 14)).place(x=620,y=70)
    tk.Label(a, text="Namakkal - 637001", fg="black", font=("Times New Roman", 14)).place(x=620,y=93)
    tk.Label(a, text="TamilNadu", fg="black", font=("Times New Roman", 14)).place(x=620,y=113)
    tk.Label(a, text="TAX INVOICE No - KA2639", fg="black", font=("Times New Roman", 18)).place(x=20,y=15)
    # Customer Order Details
    tk.Label(a, text="Customer Name", fg="black", font=("Times New Roman", 18)).place(x=20,y=120)
    tk.Label(a, text="Address", fg="black", font=("Times New Roman", 18)).place(x=20,y=160)
    tk.Label(a, text="Laptop Name", font=("bold", 18)).place(x=500,y=250)
    tk.Label(a, text="Colour", font=("bold", 18)).place(x=500,y=300)
    tk.Label(a, text="Screen Size", font=("bold", 18)).place(x=500,y=350)
    tk.Label(a, text="Processor", font=("bold", 18)).place(x=500,y=400)
    tk.Label(a, text="Specification", font=("bold", 18)).place(x=500,y=450)
    tk.Label(a, text="Payment method", font=("bold", 18)).place(x=500,y=500)
    tk.Label(a, text="phone number", font=("Times New Roman", 18)).place(x=20,y=200)
    tk.Label(a, text="Date", fg="black", font=("Times New Roman", 24)).place(x=1155,y=13)
    tk.Label(a, text="Extra Accessories", fg="black", font=("Times New Roman", 24)).place(x=1250,y=100)
    tk.Label(a, text="Thanking you for purchasing", fg="black", font=("Times New Roman", 24)).place(x=580,y=725)

    b1=tk.Entry(a,font=("cambria",13))
    b1.place(x=200,y=125)
    b2=tk.Entry(a,font=("cambria",13))
    b2.place(x=200,y=165)
    b3=tk.Entry(a,font=("cambria",13))
    b3.place(x=200,y=205)

    b4=tk.Entry(a,font=("cambria",14))
    b4.place(x=750,y=250)
    b5=ttk.Combobox(a,font=("cambria",14))
    b5['values'] = ('Blue','Red','White','Black')
    b5.place(x=750,y=300)
    b5=ttk.Combobox(a,font=("cambria",14))
    b5['values'] = ('11 Inch','12 Inch','13 Inch','14 Inch','15 Inch','16 Inch')
    b5.set("Inches")
    b5.place(x=750,y=350)
    b7=ttk.Combobox(a,font=("cambria",14))
    b7['values'] = ('intel core  i5','intel core  i6','intel core  i7','intel core  i8','intel core  i9','intel core  i10','intel core  i11')
    b7.set("Type")
    b7.place(x=750,y=400)
    b8=ttk.Combobox(a,font=("cambria",14))
    b8['values'] = ('2GB ram 500GB hard disk','4GB ram 500GB hard disk','6GB ram 500GB hard disk','8GB ram 500GB hard disk')
    b8.set("Storage")
    b8.place(x=750,y=450)
    b9=tk.Checkbutton(a,font=("cambria",15),text="Cash").place(x=750,y=500)
    b9=tk.Checkbutton(a,font=("cambria",15),text="Online").place(x=820,y=500)
    b9=tk.Checkbutton(a,font=("cambria",15),text="EMI").place(x=910,y=500)
    b11=tk.Entry(a,font=("cambria",15))
    b11.place(x=1240,y=15)

    tk.Button(a,font=("cambria",16),command=sign, text="Confirm").place(x=690,y=600)

    # Extra Accessories
    b12=tk.Checkbutton(a,font=("cambria",15),text="Bag").place(x=1300,y=150)
    b12=tk.Checkbutton(a,font=("cambria",15),text="Pendrive").place(x=1300,y=200)
    b12=tk.Checkbutton(a,font=("cambria",15),text="Speaker").place(x=1300,y=250)
    b12=tk.Checkbutton(a,font=("cambria",15),text="Pendrive Hub").place(x=1300,y=300)
    b12=tk.Checkbutton(a,font=("cambria",15),text="Mouse").place(x=1300,y=350)
    b12=tk.Checkbutton(a,font=("cambria",15),text="Keyboard").place(x=1300,y=400)
    tk.Button(a,font=("cambria",16), text="Add").place(x=1250,y=450)
    
def sign():
    messagebox.showinfo("Confirm "," Are you sure to confirm  the details")
    
app=tk.Tk()
app.title("Login")


'''image =Image.open("C:\\Users\\D.Karthik\\OneDrive\\Pictures\\murgan.jpg")
pic = ImageTk.PhotoImage(image)
tk.Label(app,image=pic).pack()'''

# Create labels and entry widgets
tk.Label(app,text="Laptop Showroom",fg="red",font=("mv Boli",30)).place(x=520,y=5)
tk.Label(app, text="Username:",fg="black",font=("bold",25)).place(x=450,y=100)

entry_username = tk.Entry(app,font=("cambria",16))
entry_username.place(x=700,y=113)

tk.Label(app, text="Password:",fg="black",font=("bold",25)).place(x=450,y=200) 
entry_password = tk.Entry(app, font=("cambria",16),show="*")
entry_password.place(x=700,y=211)

# Create login button
tk.Button(app, text="Login", command=Laptop_Showroom,fg="black",font=("cambria",15)).place(x=625,y=300)

app.mainloop()
