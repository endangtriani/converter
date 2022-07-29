import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

def Massa():
    root = Tk()
    root.title("Massa Converter")
    root.geometry("300x300")
    
    mainframe = Frame(root)
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Massa Converter", font = ("Arial", 12, "bold"), justify = CENTER).pack(padx=80, pady=20)

    text = tk.Entry(mainframe, width=23, bd=4)
    text.place(x=85, y = 80)

    menu = StringVar()
    data = ["Kilogram","Gram","Miligram","ons","kuintal","ton"]
    combo1 = ttk.Combobox(mainframe, values=data, textvariable=menu)
    combo1.set("Pick an Option")
    combo1.place(x=85, y=110)
   

    text2 = tk.Entry(mainframe, width=23, bd=4)
    text2.place(x=85, y = 200)

    menu2 = StringVar()
    mList2 = ["Kilogram","Gram","Miligram","ons","kuintal","ton"]
    combo2 = ttk.Combobox(mainframe, values= mList2, textvariable=menu2)
    combo2.set("Pick an Option")
    combo2.place(x=85, y=230)

    
    def callback():  
     try:

        if combo1.get() == "Pick an Option" or combo2.get() == "Pick an Option":
            messagebox.showinfo("showinfo","Input or output unit not chosen")
        elif combo1.get() == "Kilogram":
            nilai = 0
            if combo2.get() == "Kilogram":    
                nilai +=float(text.get())
            elif combo2.get() == "Gram":
               nilai +=float(text.get())*1000
            elif combo2.get() == "Miligram":
               nilai +=float(text.get())*1000000
            elif combo2.get() == "ons":
               nilai +=float(text.get())*10
            elif combo2.get() == "kuintal":
               nilai +=float(text.get())*0.01
            elif combo2.get() == "ton":
               nilai +=float(text.get())*0.001

        elif combo1.get() == "Gram":
            nilai = 0
            if combo2.get() == "Gram":    
                nilai +=float(text.get())
            elif combo2.get() == "Kilogram":
               nilai +=float(text.get())*0.001
            elif combo2.get() == "Miligram":
               nilai +=float(text.get())*1000
            elif combo2.get() == "ons":
               nilai +=float(text.get())*0.01
            elif combo2.get() == "kuintal":
               nilai +=float(text.get())*0.00001
            elif combo2.get() == "ton":
               nilai +=float(text.get())*0.000001

        elif combo1.get() == "Miligram":
            nilai = 0
            if combo2.get() == "Miligram":    
                nilai +=float(text.get())
            elif combo2.get() == "Kilogram":
               nilai +=float(text.get())*0.000001
            elif combo2.get() == "Gram":
               nilai +=float(text.get())*0.001
            elif combo2.get() == "ons":
               nilai +=float(text.get())*0.00001
            elif combo2.get() == "kuintal":
               nilai +=float(text.get())*0.00000001
            elif combo2.get() == "ton":
               nilai +=float(text.get())*0.000000001

        elif combo1.get() == "ons":
            nilai = 0
            if combo2.get() == "ons":    
                nilai +=float(text.get())
            elif combo2.get() == "Kilogram":
               nilai +=float(text.get())*0.1
            elif combo2.get() == "Gram":
               nilai +=float(text.get())*100
            elif combo2.get() == "Miligram":
               nilai +=float(text.get())*100000
            elif combo2.get() == "kuintal":
               nilai +=float(text.get())*0.001
            elif combo2.get() == "ton":
               nilai +=float(text.get())*0.0001

        elif combo1.get() == "kuintal":
            nilai = 0
            if combo2.get() == "kuintal":    
                nilai +=float(text.get())
            elif combo2.get() == "Kilogram":
               nilai +=float(text.get())*100
            elif combo2.get() == "Gram":
               nilai +=float(text.get())*100000
            elif combo2.get() == "Miligram":
               nilai +=float(text.get())*100000000
            elif combo2.get() == "ons":
               nilai +=float(text.get())*1000
            elif combo2.get() == "ton":
               nilai +=float(text.get())*0.1

        elif combo1.get() == "ton":
            nilai = 0
            if combo2.get() == "ton":    
                nilai +=float(text.get())
            elif combo2.get() == "Kilogram":
               nilai +=float(text.get())*1000
            elif combo2.get() == "Gram":
               nilai +=float(text.get())*1000000
            elif combo2.get() == "Miligram":
               nilai +=float(text.get())*1000000000
            elif combo2.get() == "ons":
               nilai +=float(text.get())*10000
            elif combo2.get() == "kuintal":
               nilai +=float(text.get())*10



        text2.delete("0",END)
        text2.insert(END,round(nilai,2))             
        return nilai
     except ValueError:
        messagebox.showinfo("Error", "Invalid syntax")
        return None

    cal_button = tk.Button(mainframe, text = "Calculate", command=callback)
    cal_button.place(x=130, y = 160)

    root.resizable(False,False)
    

def Panjang():
    root = Tk()
    root.title("Panjang Converter")
    root.geometry("300x300")
    
    mainframe = Frame(root)
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Panjang", font = ("Arial", 12, "bold"), justify = CENTER).pack(padx=80, pady=20)

    text = tk.Entry(mainframe, width=23, bd=4)
    text.place(x=85, y = 80)

    menu = StringVar()
    data = ["km", "m","cm","mm","mil","yard","kaki","inci"]
    combo1 = ttk.Combobox(mainframe, values=data, textvariable=menu)
    combo1.set("Pick an Option")
    combo1.place(x=85, y=110)
   

    text2 = tk.Entry(mainframe, width=23, bd=4)
    text2.place(x=85, y=200)

    menu2 = StringVar()
    mList2 = ["km", "m","cm","mm","mil","yard","kaki","inci"]
    combo2 = ttk.Combobox(mainframe, values= mList2, textvariable=menu2)
    combo2.set("Pick an Option")
    combo2.place(x=85, y=230)

    
    def callback():    
        if combo1.get() == "Pick an Option" or combo2.get() == "Pick an Option":
            messagebox.showinfo("showinfo","Input or output unit not chosen")
        else:
            try:
               #masukan program di sini
                txt= text.get()
                opt1 = combo1.get()
                opt2 = combo2.get()
                if opt1 == "km" and opt2 == "m":
                    hasil = float(txt)*1000
                    text2.insert(0,round(hasil,2))
                elif opt1 == "km" and opt2 == "cm":
                    hasil = float(txt)*100000
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "km" and opt2 == "mm":
                    hasil = float(txt)*1000000
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "km" and opt2 == "mil":
                    hasil = float(txt)*0.621371
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "km" and opt2 == "yard":
                    hasil = float(txt)*1093.61
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "km" and opt2 == "kaki":
                    hasil = float(txt)*3280.84
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "km" and opt2 == "inci":
                    hasil = float(txt)*39370.1
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "m" and opt2 == "km":
                    hasil = float(txt)/1000
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "m" and opt2 == "cm":
                    hasil = float(txt)*100
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "m" and opt2 == "mm":
                    hasil = float(txt)*1000
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "m" and opt2 == "mil":
                    hasil = float(txt)*0.000621371
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "m" and opt2 == "yard":
                    hasil = float(txt)*1.09361
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "m" and opt2 == "kaki":
                    hasil = float(txt)*3.28084
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "m" and opt2 == "inci":
                    hasil = float(txt)*39.3701
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "cm" and opt2 == "km":
                    hasil = float(txt)/100000
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "cm" and opt2 == "m":
                    hasil = float(txt)/100
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "cm" and opt2 == "mm":
                    hasil = float(txt)*10
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "cm" and opt2 == "mil":
                    hasil = float(txt)/160934
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "cm" and opt2 == "yard":
                    hasil = float(txt)/91.44
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "cm" and opt2 == "kaki":
                    hasil = float(txt)/30.48
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "cm" and opt2 == "inci":
                    hasil = float(txt)/2.54
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "mm" and opt2 == "km":
                    hasil = float(txt)/1000000
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "mm" and opt2 == "m":
                    hasil = float(txt)/1000
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "mm" and opt2 == "cm":
                    hasil = float(txt)/10
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "mm" and opt2 == "mil":
                    hasil = float(txt)*0.000000621371
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "mm" and opt2 == "yard":
                    hasil = float(txt)/914
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "mm" and opt2 == "kaki":
                    hasil = float(txt)/305
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "mm" and opt2 == "inci":
                    hasil = float(txt)/25.4
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "mil" and opt2 == "km":
                    hasil = float(txt)*1.609
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "mil" and opt2 == "m":
                    hasil = float(txt)*1609
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "mil" and opt2 == "cm":
                    hasil = float(txt)*160934
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "mil" and opt2 == "mm":
                    hasil = float(txt)*1609340
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "mil" and opt2 == "yard":
                    hasil = float(txt)*1760
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "mil" and opt2 == "kaki":
                    hasil = float(txt)*5280
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "mil" and opt2 == "inci":
                    hasil = float(txt)*63360
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "yard" and opt2 == "km":
                    hasil = float(txt)/1094
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "yard" and opt2 == "m":
                    hasil = float(txt)/1.094
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "yard" and opt2 == "cm":
                    hasil = float(txt)*91.44
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "yard" and opt2 == "mm":
                    hasil = float(txt)*914
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "yard" and opt2 == "mil":
                    hasil = float(txt)/1760
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "yard" and opt2 == "kaki":
                    hasil = float(txt)*3
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "yard" and opt2 == "inci":
                    hasil = float(txt)*36
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "kaki" and opt2 == "km":
                    hasil = float(txt)/3281
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "kaki" and opt2 == "m":
                    hasil = float(txt)/3.281
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "kaki" and opt2 == "cm":
                    hasil = float(txt)*30.48
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "kaki" and opt2 == "mm":
                    hasil = float(txt)*305
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "kaki" and opt2 == "mil":
                    hasil = float(txt)/5280
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "kaki" and opt2 == "yard":
                    hasil = float(txt)*3
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "kaki" and opt2 == "inci":
                    hasil = float(txt)*12
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "inci" and opt2 == "km":
                    hasil = float(txt)/39370
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "inci" and opt2 == "m":
                    hasil = float(txt)/39.37
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "inci" and opt2 == "cm":
                    hasil = float(txt)*2.54
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "inci" and opt2 == "mm":
                    hasil = float(txt)* 25.4
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "inci" and opt2 == "mil":
                    hasil = float(txt)/63360
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "inci" and opt2 == "yard":
                    hasil = float(txt)/36
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "inci" and opt2 == "kaki":
                    hasil = float(txt)/12
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
            except ValueError:
                messagebox.showinfo("Error", "Invalid syntax")
                return None

    cal_button = tk.Button(mainframe, text = "Calculate", command=callback)
    cal_button.place(x=130, y = 160)

    root.resizable(False,False)
    
def Waktu():
    root = Tk()
    root.title("Waktu Converter")
    root.geometry("300x300")
    
    mainframe = Frame(root)
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Waktu", font = ("Arial", 12, "bold"), justify = CENTER).pack(padx=80, pady=20)

    text = tk.Entry(mainframe, width=23, bd=4)
    text.place(x=85, y = 80)

    menu = StringVar()
    data = ["hari", "jam","menit","detik","microdetik"]
    combo1 = ttk.Combobox(mainframe, values=data, textvariable=menu)
    combo1.set("Pick an Option")
    combo1.place(x=85, y=110)
   

    text2 = tk.Entry(mainframe, width=23, bd=4)
    text2.place(x=85, y=200)

    menu2 = StringVar()
    mList2 = ["hari", "jam","menit","detik","microdetik"]
    combo2 = ttk.Combobox(mainframe, values= mList2, textvariable=menu2)
    combo2.set("Pick an Option")
    combo2.place(x=85, y=230)

    def callback():  
        try:

            if combo1.get() == "Pick an Option" or combo2.get() == "Pick an Option":
                messagebox.showinfo("showinfo","Input or output unit not chosen")
            elif combo1.get() == "hari":
                nilai = 0
                if combo2.get() == "hari":    
                    nilai +=float(text.get())
                elif combo2.get() == "jam":
                    nilai +=float(text.get())*24
                elif combo2.get() == "menit":
                    nilai +=float(text.get())*1440
                elif combo2.get() == "detik":
                    nilai +=float(text.get())*86400
                elif combo2.get() == "microdetik":
                    nilai +=float(text.get())*864000000

            elif combo1.get() == "jam":
                nilai = 0
                if combo2.get() == "jam":
                    nilai +=float(text.get())
                elif combo2.get() == "hari":    
                    nilai +=float(text.get())*0.0417
                elif combo2.get() == "menit":
                    nilai +=float(text.get())*60
                elif combo2.get() == "detik":
                    nilai +=float(text.get())*3600
                elif combo2.get() == "microdetik":
                    nilai +=float(text.get())*3600000000

            elif combo1.get() == "menit":
                nilai = 0
                if combo2.get() == "menit":
                    nilai +=float(text.get())
                elif combo2.get() == "jam":
                    nilai +=float(text.get())*0.0167
                elif combo2.get() == "hari":    
                    nilai +=float(text.get())*0.0000694
                elif combo2.get() == "detik":
                    nilai +=float(text.get())*60
                elif combo2.get() == "microdetik":
                    nilai +=float(text.get())*600000000

            elif combo1.get() == "detik":
                nilai = 0
                if combo2.get() == "detik":
                    nilai +=float(text.get())
                elif combo2.get() == "jam":
                    nilai +=float(text.get())*0.0000278
                elif combo2.get() == "menit":
                    nilai +=float(text.get())*0.0167
                elif combo2.get() == "hari":    
                    nilai +=float(text.get())*0.00000116
                elif combo2.get() == "microdetik":
                    nilai +=float(text.get())*1000000

            elif combo1.get() == "microdetik":
                nilai = 0
                if combo2.get() == "microdetik":
                    nilai +=float(text.get())
                elif combo2.get() == "jam":
                    nilai +=float(text.get())*0.000000000278
                elif combo2.get() == "menit":
                    nilai +=float(text.get())*0.0000000167
                elif combo2.get() == "detik":
                    nilai +=float(text.get())*0.000001
                elif combo2.get() == "hari":    
                    nilai +=float(text.get())*0.0000000000116
            text2.delete("0",END)
            text2.insert(END,round(nilai,2))              
            return nilai
        except ValueError:
            messagebox.showinfo("Error", "Invalid syntax")
            return None

    cal_button = tk.Button(mainframe, text = "Calculate", command=callback)
    cal_button.place(x=130, y = 160)

    root.resizable(False,False)

def Suhu():
    root = Tk()
    root.title("Suhu Converter")
    root.geometry("300x300")
    
    mainframe = Frame(root)
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Suhu", font = ("Arial", 12, "bold"), justify = CENTER).pack(padx=80, pady=20)

    text = tk.Entry(mainframe, width=23, bd=4)
    text.place(x=85, y = 80)

    menu = StringVar()
    data = ["Celcius", "Fahrenheit","Kelvin","Reamur"]
    combo1 = ttk.Combobox(mainframe, values=data, textvariable=menu)
    combo1.set("Pick an Option")
    combo1.place(x=85, y=110)
   

    text2 = tk.Entry(mainframe, width=23, bd=4)
    text2.place(x=85, y=200)

    menu2 = StringVar()
    mList2 = ["Celcius", "Fahrenheit","Kelvin","Reamur"]
    combo2 = ttk.Combobox(mainframe, values= mList2, textvariable=menu2)
    combo2.set("Pick an Option")
    combo2.place(x=85, y=230)

    
    def callback():    
        if combo1.get() == "Pick an Option" or combo2.get() == "Pick an Option":
            messagebox.showinfo("showinfo","Input or output unit not chosen")
        else:
            try:
                txt= text.get()
                opt1 = combo1.get()
                opt2 = combo2.get()
                if opt1 == "Celcius" and opt2 == "Fahrenheit":
                    hasil = (9/5)*float(txt)+32
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Celcius" and opt2 == "Kelvin":
                    hasil = float(txt)+273.15
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Celcius" and opt2 == "Reamur":
                    hasil = (4/5)*float(txt)
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Celcius" and opt2 == "Celcius":
                    hasil = float(txt)
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "Fahrenheit" and opt2 == "Celcius":
                    hasil = (float(txt)-32)*(5/9)
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Fahrenheit" and opt2 == "Kelvin":
                    hasil = (float(txt)+459.67)*(5/9)
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Fahrenheit" and opt2 == "Reamur":
                    hasil = (4/9)*(float(txt-32))
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Fahrenheit" and opt2 == "Fahrenheit":
                    hasil = float(txt)
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "Kelvin" and opt2 == "Celcius":
                    hasil = float(txt)-273.15
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Kelvin" and opt2 == "Fahrenheit":
                    hasil = (9/5*float(txt))-459.67
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Kelvin" and opt2 == "Reamur":
                    hasil = (4/5)*(float(txt)-273.15)
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Kelvin" and opt2 == "Kelvin":
                    hasil = float(txt)
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                elif opt1 == "Reamur" and opt2 == "Celcius":
                    hasil = float(txt)/0.8
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Reamur" and opt2 == "Fahrenheit":
                    hasil = (float(txt)*2.25)+32
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Reamur" and opt2 == "Kelvin":
                    hasil = (float(txt)/0.8)+ 273.15
                    text2.delete(0, END)
                    text2.insert(0,round(hasil,2))
                elif opt1 == "Reamur" and opt2 == "Reamur":
                    hasil = float(txt)
                    text2.delete(0, END)
                    text2.insert(0, round(hasil,2))
                    
                
            except ValueError:
                messagebox.showinfo("Error", "Invalid syntax")
                return None

    cal_button = tk.Button(mainframe, text = "Calculate", command=callback)
    cal_button.place(x=130, y = 160)

    root.resizable(False,False)

 
root = tk.Tk()
root.title("Unit Converter App")
root.geometry("500x500")
l = Label(root, text="Unit Converter App", font=("Calibri", 15, 'bold'), justify=CENTER).pack(padx=80, pady=20)
widget = tk.Button(None, text="QUIT", bg="white", fg="red",font = ("Calibri", 12, "bold"), relief = "raised", bd=5, justify = CENTER, highlightbackground = "red", command=root.destroy).place(x=415,y=400)
widget = tk.Button(None, text="MASSA", bg="white", fg="red", width=50, font = ("Calibri", 12, "bold"), relief = "raised", bd=5, justify = CENTER, command=Massa).place(x=50,y=120)
widget = tk.Button(None, text="PANJANG", bg="white", fg="red", width=50, font = ("Calibri", 12, "bold"), relief = "raised", bd=5, justify = CENTER, command=Panjang).place(x=50,y=180)
widget = tk.Button(None, text="WAKTU", bg="white", fg="red", width=50, font = ("Calibri", 12, "bold"), relief = "raised", bd=5, justify = CENTER, command=Waktu).place(x=50,y=240)
widget = tk.Button(None, text="SUHU", bg="white", fg="red", width=50, font = ("Calibri", 12, "bold"), relief = "raised", bd=5, justify = CENTER, command=Suhu).place(x=50,y=300)


root.mainloop()
