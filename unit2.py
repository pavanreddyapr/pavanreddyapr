from tkinter import * 
from tkinter import  ttk
from tkinter import messagebox

#Weight_Converter
def weight_converter():

    #cearte cli
    def convert():
        
        input_get=input_value.get()
        cb1_get= cb1.get()
        cb2_get= cb2.get()
        


        if cb1_get =='Kilogram (kg)':
            cb1_get = 1
            #print(cb1_get)
        elif cb1_get=='Gram (g)':
            cb1_get = 2
            #print(cb1_get)
        elif cb1_get== 'Pound (Ib)':
            cb1_get = 3
            #print(cb1_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb1_get)


        if cb2_get =='Kilogram (kg)':
            cb2_get = 1
            #print(cb2_get)
        elif cb2_get=='Gram (g)':
            cb2_get = 2
            #print(cb2_get)
        elif cb2_get== 'Pound (Ib)':
            cb2_get = 3
            #print(cb2_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb2_get)

    
        if cb1_get==1 and cb2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Kg')
            
        elif cb1_get==1 and cb2_get==2:
            value = input_get*1000
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' g')
            

        elif cb1_get==1 and cb2_get==3:
            output.delete(1.0,END)
            value = input_get*2.20462
            output.insert('end',value)
            output.insert('end',' Pound')

        elif cb1_get==2 and cb2_get==1:
            output.delete(1.0,END)
            value = input_get/1000
            output.insert('end',value)
            output.insert('end',' Kg')
        
        elif cb1_get==2 and cb2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' g')
        
        elif cb1_get==2 and cb2_get==3:
            output.delete(1.0,END)
            value = input_get/454
            output.insert('end',value)
            output.insert('end',' Pound')
        
        if cb1_get==3 and cb2_get==1:
            output.delete(1.0,END)
            value = input_get/2.205
            output.insert('end',value)
            output.insert('end',' Kg')
        
        elif cb1_get==3 and cb2_get==2:
            output.delete(1.0,END)
            value= input_get*454
            output.insert('end',value)
            output.insert('end',' g')
        
        elif cb1_get==3 and cb2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Pound')

    #create gui
    root = Tk()
    root.title('Weight Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Weight Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter Value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value = DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'Kilogram (kg)','Gram (g)','Pound (Ib)'
    ] 

    cb1 = ttk.Combobox(root,values=unit_list)
    cb1.set('Kilogram (kg)')
    cb1.place(x=150,y= 115)


    cb2 = ttk.Combobox(root,values=unit_list)
    cb2.set('Gram (g)')
    cb2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 128, y =270 )
    
    
    root.mainloop()

#length converter
def length_converter():
    #cearte cli
    def convert():
        
        input_get=input_value.get()
        cb1_get= cb1.get()
        cb2_get= cb2.get()
        


        if cb1_get =='Kilometre (km)':
            cb1_get = 1
            #print(cb1_get)
        elif cb1_get=='Metre (m)':
            cb1_get = 2
            #print(cb1_get)
        elif cb1_get== 'Centimeter (Cm)':
            cb1_get = 3
            #print(cb1_get)
        elif cb1_get== 'Inch (In)':
            cb1_get = 4
            #print(cb2_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb1_get)


        if cb2_get =='Kilometre (km)':
            cb2_get = 1
            #print(cb2_get)
        elif cb2_get=='Metre (m)':
            cb2_get = 2
            #print(cb2_get)
        elif cb2_get== 'Centimeter (Cm)':
            cb2_get = 3
            #print(cb2_get)
        elif cb2_get== 'Inch (In)':
            cb2_get = 4
            #print(cb2_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb2_get)

    
        if cb1_get==1 and cb2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Km')
        elif cb1_get==1 and cb2_get==2:
            value = input_get*1000
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' m')
        elif cb1_get==1 and cb2_get==3:
            output.delete(1.0,END)
            value = input_get*100000
            output.insert('end',value)
            output.insert('end',' Cm')
        elif cb1_get==1 and cb2_get==4:
            output.delete(1.0,END)
            value = input_get*39370
            output.insert('end',value)
            output.insert('end',' Inch')

        elif cb1_get==2 and cb2_get==1:
            output.delete(1.0,END)
            value = input_get/1000
            output.insert('end',value)
            output.insert('end',' Km')
        elif cb1_get==2 and cb2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' m')
        elif cb1_get==2 and cb2_get==3:
            output.delete(1.0,END)
            value = input_get*100
            output.insert('end',value)
            output.insert('end',' Cm')
        elif cb1_get==2 and cb2_get==4:
            output.delete(1.0,END)
            value = input_get*39.37
            output.insert('end',value)
            output.insert('end',' Inch')

        if cb1_get==3 and cb2_get==1:
            output.delete(1.0,END)
            value = input_get/100000
            output.insert('end',value)
            output.insert('end',' Km')
        elif cb1_get==3 and cb2_get==2:
            output.delete(1.0,END)
            value= input_get/100
            output.insert('end',value)
            output.insert('end',' m')
        elif cb1_get==3 and cb2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Cm')
        elif cb1_get==3 and cb2_get==4:
            output.delete(1.0,END)
            value = input_get/2.54
            output.insert('end',value)
            output.insert('end',' Inch')
        
        elif cb1_get==4 and cb2_get==1:
            output.delete(1.0,END)
            value= input_get*39370
            output.insert('end',value)
            output.insert('end',' Km')
        elif cb1_get==4 and cb2_get==2:
            output.delete(1.0,END)
            value= input_get/39.37
            output.insert('end',value)
            output.insert('end',' m')
        elif cb1_get==4 and cb2_get==3:
            output.delete(1.0,END)
            value= input_get*2.54
            output.insert('end',value)
            output.insert('end',' Cm')
        elif cb1_get==4 and cb2_get==4:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Inch')
            


    #create gui
    root = Tk()
    root.title('Length Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Length Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter Value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value = DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'Kilometre (km)','Metre (m)','Centimeter (Cm)','Inch (In)'
    ] 

    cb1 = ttk.Combobox(root,values=unit_list)
    cb1.set('Kilometre (km)')
    cb1.place(x=150,y= 115)


    cb2 = ttk.Combobox(root,values=unit_list)
    cb2.set('Metre (m)')
    cb2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 128, y =270 )
    
    
    root.mainloop()

#Time converter
def time_convert():
    def convert():
        
        input_get=input_value.get()
        cb1_get= cb1.get()
        cb2_get= cb2.get()
        


        if cb1_get =='Celsius (°C)':
            cb1_get = 1
            #print(cb1_get)
        elif cb1_get=='Fahrenheit (°F)':
            cb1_get = 2
            #print(cb1_get)
        elif cb1_get== 'Kelvin (°K)':
            cb1_get = 3
            #print(cb1_get)
        
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb1_get)


        if cb2_get =='Celsius (°C)':
            cb2_get = 1
            #print(cb2_get)
        elif cb2_get=='Fahrenheit (°F)':
            cb2_get = 2
            #print(cb2_get)
        elif cb2_get== 'Kelvin (°K)':
            cb2_get = 3
            #print(cb2_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb2_get)
        
        if cb1_get==1 and cb2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °C')
        elif cb1_get==1 and cb2_get==2:
            value = (input_get*9/5)+32
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' °F')
        elif cb1_get==1 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get+ 273.15)
            output.insert('end',value)
            output.insert('end',' °K')
        
        if cb1_get==2 and cb2_get==1:
            value = (input_get-32)*5/9
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' °C')
        elif cb1_get==2 and cb2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °F')
        elif cb1_get==2 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get-32)*5/9+273.15
            output.insert('end',value)
            output.insert('end',' °K')
        
        if cb1_get==3 and cb2_get==1:
            value = (input_get-273.15)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' °C')
        elif cb1_get==3 and cb2_get==2:
            value = (input_get - 273.15) * 9/5 + 32
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' °F')
        elif cb1_get==3 and cb2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °K')



        #create gui
    root = Tk()
    root.title('Temperature Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Temperature Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter Value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value = DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'Celsius (°C)','Fahrenheit (°F)','Kelvin (°K)',
    ] 

    cb1 = ttk.Combobox(root,values=unit_list)
    cb1.set('Celsius (°C)')
    cb1.place(x=150,y= 115)


    cb2 = ttk.Combobox(root,values=unit_list)
    cb2.set('Fahrenheit (°F)')
    cb2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 128, y =270 )
    
    
    root.mainloop()


#digital storage conver
def digital_storage_convert():
    def convert():
        
        input_get=input_value.get()
        cb1_get= cb1.get()
        cb2_get= cb2.get()
        


        if cb1_get =='Bits':
            cb1_get = 1
        elif cb1_get=='Bytes':
            cb1_get = 2
        elif cb1_get== 'Kilobytes':
            cb1_get = 3
        elif cb1_get== 'Megabytes':
            cb1_get = 4
        elif cb1_get== 'Gigabytes':
            cb1_get = 5
        elif cb1_get== 'Terabytes':
            cb1_get = 6
        elif cb1_get== 'Petabytes':
            cb1_get = 7
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb1_get)


        if cb2_get =='Bits':
            cb2_get = 1
        elif cb2_get=='Bytes':
            cb2_get = 2
        elif cb2_get== 'Kilobytes':
            cb2_get = 3
        elif cb2_get== 'Megabytes':
            cb2_get = 4
        elif cb2_get== 'Gigabytes':
            cb2_get = 5
        elif cb2_get== 'Terabytes':
            cb2_get = 6
        elif cb2_get== 'Petabytes':
            cb2_get = 7
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb2_get)
        

        if cb1_get==1 and cb2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Bits')
        elif cb1_get==1 and cb2_get==2:
            value = (input_get/8)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==1 and cb2_get==3:
            output.delete(1.0,END)
            value = ((input_get/8)/(1024))
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==1 and cb2_get==4:
            output.delete(1.0,END)
            value = ((input_get/8)*0.000001 )
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==1 and cb2_get==5:
            output.delete(1.0,END)
            value = (input_get/8000000000)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==1 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/8e+12)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==1 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/ 8e+15)
            output.insert('end',value)
            output.insert('end',' Pb')


        if cb1_get==2 and cb2_get==1:
            value = (input_get*8)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==2 and cb2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Bytes')
        elif cb1_get==2 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*0.0009765625)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==2 and cb2_get==4:
            output.delete(1.0,END)
            value = (input_get/1024/1024)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==2 and cb2_get==5:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==2 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==2 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Pb')

        if cb1_get==3 and cb2_get==1:
            value = (input_get*8192)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==3 and cb2_get==2:
            value = (input_get*1024)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==3 and cb2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Kb')
        elif cb1_get==3 and cb2_get==4:
            output.delete(1.0,END)
            value = (input_get/1024)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==3 and cb2_get==5:
            output.delete(1.0,END)
            value = (input_get/1024/1024)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==3 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==3 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Pb')

        if cb1_get==4 and cb2_get==1:
            value = (input_get*8388608)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==4 and cb2_get==2:
            value = (input_get*1048576)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==4 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*1024)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==4 and cb2_get==4:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Mb')
        elif cb1_get==4 and cb2_get==5:
            output.delete(1.0,END)
            value = (input_get/1024)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==4 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/1024/1024)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==4 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Pb')
        
        if cb1_get==5 and cb2_get==1:
            value = (input_get*8589934592)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==5 and cb2_get==2:
            value = (input_get*1073741824)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==5 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*1048576)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==5 and cb2_get==4:
            value = (input_get *1024)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==5 and cb2_get==5:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Gb')
        elif cb1_get==5 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/1024)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==5 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024/1024)
            output.insert('end',value)
            output.insert('end',' Pb')

        if cb1_get==6 and cb2_get==1:
            value = (input_get*8796093022208)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==6 and cb2_get==2:
            value = (input_get*1099511627776)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==6 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*1073741824)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==6 and cb2_get==4:
            value = (input_get *1048576)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==6 and cb2_get==5:
            value = (input_get*1024)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==6 and cb2_get==6:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Tb')
        elif cb1_get==6 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024)
            output.insert('end',value)
            output.insert('end',' Pb')
        
        if cb1_get==7 and cb2_get==1:
            value = (input_get*9007199254740992)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==7 and cb2_get==2:
            value = (input_get*1125899906842624)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==7 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*1099511627776)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==7 and cb2_get==4:
            value = (input_get *1073741824)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==7 and cb2_get==5:
            value = (input_get*1048576)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==7 and cb2_get==6:
            value = (input_get*1024)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==7 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get)
            output.insert('end',value)
            output.insert('end',' Pb')
        


        #create gui
    root = Tk()
    root.title('Digital storage Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Digital storage Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter Value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value = DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'Bits','Bytes','Kilobytes','Megabytes','Gigabytes','Terabytes','Petabytes',
    ] 

    cb1 = ttk.Combobox(root,values=unit_list)
    cb1.set('Bits')
    cb1.place(x=150,y= 115)


    cb2 = ttk.Combobox(root,values=unit_list)
    cb2.set('Bytes')
    cb2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 128, y =270 )
    
    
    root.mainloop()



#create screen
screen = Tk() 
screen.geometry('200x180')
screen.title('My Converters')
screen.resizable(0,0)
screen.configure(bg='#68999c')

#create butto
m_c = Button(text='Digital Storage Converter',command=digital_storage_convert).place(x= 20, y= 20)
l_c = Button(text='       Length converter       ',command=length_converter).place(x=20,y= 50)
t_c = Button(text='  Temperature converter  ',command=time_convert).place(x=20,y= 80)
w_c = Button(text='       Weight converter       ',command=weight_converter).place(x=20,y= 110)

#create text
Label(text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 20, y = 150)

screen.mainloop()
from tkinter import * 
from tkinter import  ttk
from tkinter import messagebox

#Weight_Converter
def weight_converter():

    #cearte cli
    def convert():
        
        input_get=input_value.get()
        cb1_get= cb1.get()
        cb2_get= cb2.get()
        


        if cb1_get =='Kilogram (kg)':
            cb1_get = 1
            #print(cb1_get)
        elif cb1_get=='Gram (g)':
            cb1_get = 2
            #print(cb1_get)
        elif cb1_get== 'Pound (Ib)':
            cb1_get = 3
            #print(cb1_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb1_get)


        if cb2_get =='Kilogram (kg)':
            cb2_get = 1
            #print(cb2_get)
        elif cb2_get=='Gram (g)':
            cb2_get = 2
            #print(cb2_get)
        elif cb2_get== 'Pound (Ib)':
            cb2_get = 3
            #print(cb2_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb2_get)

    
        if cb1_get==1 and cb2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Kg')
            
        elif cb1_get==1 and cb2_get==2:
            value = input_get*1000
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' g')
            

        elif cb1_get==1 and cb2_get==3:
            output.delete(1.0,END)
            value = input_get*2.20462
            output.insert('end',value)
            output.insert('end',' Pound')

        elif cb1_get==2 and cb2_get==1:
            output.delete(1.0,END)
            value = input_get/1000
            output.insert('end',value)
            output.insert('end',' Kg')
        
        elif cb1_get==2 and cb2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' g')
        
        elif cb1_get==2 and cb2_get==3:
            output.delete(1.0,END)
            value = input_get/454
            output.insert('end',value)
            output.insert('end',' Pound')
        
        if cb1_get==3 and cb2_get==1:
            output.delete(1.0,END)
            value = input_get/2.205
            output.insert('end',value)
            output.insert('end',' Kg')
        
        elif cb1_get==3 and cb2_get==2:
            output.delete(1.0,END)
            value= input_get*454
            output.insert('end',value)
            output.insert('end',' g')
        
        elif cb1_get==3 and cb2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Pound')

    #create gui
    root = Tk()
    root.title('Weight Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Weight Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter Value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value = DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'Kilogram (kg)','Gram (g)','Pound (Ib)'
    ] 

    cb1 = ttk.Combobox(root,values=unit_list)
    cb1.set('Kilogram (kg)')
    cb1.place(x=150,y= 115)


    cb2 = ttk.Combobox(root,values=unit_list)
    cb2.set('Gram (g)')
    cb2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 128, y =270 )
    
    
    root.mainloop()

#length converter
def length_converter():
    #cearte cli
    def convert():
        
        input_get=input_value.get()
        cb1_get= cb1.get()
        cb2_get= cb2.get()
        


        if cb1_get =='Kilometre (km)':
            cb1_get = 1
            #print(cb1_get)
        elif cb1_get=='Metre (m)':
            cb1_get = 2
            #print(cb1_get)
        elif cb1_get== 'Centimeter (Cm)':
            cb1_get = 3
            #print(cb1_get)
        elif cb1_get== 'Inch (In)':
            cb1_get = 4
            #print(cb2_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb1_get)


        if cb2_get =='Kilometre (km)':
            cb2_get = 1
            #print(cb2_get)
        elif cb2_get=='Metre (m)':
            cb2_get = 2
            #print(cb2_get)
        elif cb2_get== 'Centimeter (Cm)':
            cb2_get = 3
            #print(cb2_get)
        elif cb2_get== 'Inch (In)':
            cb2_get = 4
            #print(cb2_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb2_get)

    
        if cb1_get==1 and cb2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Km')
        elif cb1_get==1 and cb2_get==2:
            value = input_get*1000
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' m')
        elif cb1_get==1 and cb2_get==3:
            output.delete(1.0,END)
            value = input_get*100000
            output.insert('end',value)
            output.insert('end',' Cm')
        elif cb1_get==1 and cb2_get==4:
            output.delete(1.0,END)
            value = input_get*39370
            output.insert('end',value)
            output.insert('end',' Inch')

        elif cb1_get==2 and cb2_get==1:
            output.delete(1.0,END)
            value = input_get/1000
            output.insert('end',value)
            output.insert('end',' Km')
        elif cb1_get==2 and cb2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' m')
        elif cb1_get==2 and cb2_get==3:
            output.delete(1.0,END)
            value = input_get*100
            output.insert('end',value)
            output.insert('end',' Cm')
        elif cb1_get==2 and cb2_get==4:
            output.delete(1.0,END)
            value = input_get*39.37
            output.insert('end',value)
            output.insert('end',' Inch')

        if cb1_get==3 and cb2_get==1:
            output.delete(1.0,END)
            value = input_get/100000
            output.insert('end',value)
            output.insert('end',' Km')
        elif cb1_get==3 and cb2_get==2:
            output.delete(1.0,END)
            value= input_get/100
            output.insert('end',value)
            output.insert('end',' m')
        elif cb1_get==3 and cb2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Cm')
        elif cb1_get==3 and cb2_get==4:
            output.delete(1.0,END)
            value = input_get/2.54
            output.insert('end',value)
            output.insert('end',' Inch')
        
        elif cb1_get==4 and cb2_get==1:
            output.delete(1.0,END)
            value= input_get*39370
            output.insert('end',value)
            output.insert('end',' Km')
        elif cb1_get==4 and cb2_get==2:
            output.delete(1.0,END)
            value= input_get/39.37
            output.insert('end',value)
            output.insert('end',' m')
        elif cb1_get==4 and cb2_get==3:
            output.delete(1.0,END)
            value= input_get*2.54
            output.insert('end',value)
            output.insert('end',' Cm')
        elif cb1_get==4 and cb2_get==4:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Inch')
            


    #create gui
    root = Tk()
    root.title('Length Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Length Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter Value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value = DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'Kilometre (km)','Metre (m)','Centimeter (Cm)','Inch (In)'
    ] 

    cb1 = ttk.Combobox(root,values=unit_list)
    cb1.set('Kilometre (km)')
    cb1.place(x=150,y= 115)


    cb2 = ttk.Combobox(root,values=unit_list)
    cb2.set('Metre (m)')
    cb2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 128, y =270 )
    
    
    root.mainloop()

#Time converter
def time_convert():
    def convert():
        
        input_get=input_value.get()
        cb1_get= cb1.get()
        cb2_get= cb2.get()
        


        if cb1_get =='Celsius (°C)':
            cb1_get = 1
            #print(cb1_get)
        elif cb1_get=='Fahrenheit (°F)':
            cb1_get = 2
            #print(cb1_get)
        elif cb1_get== 'Kelvin (°K)':
            cb1_get = 3
            #print(cb1_get)
        
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb1_get)


        if cb2_get =='Celsius (°C)':
            cb2_get = 1
            #print(cb2_get)
        elif cb2_get=='Fahrenheit (°F)':
            cb2_get = 2
            #print(cb2_get)
        elif cb2_get== 'Kelvin (°K)':
            cb2_get = 3
            #print(cb2_get)
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb2_get)
        
        if cb1_get==1 and cb2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °C')
        elif cb1_get==1 and cb2_get==2:
            value = (input_get*9/5)+32
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' °F')
        elif cb1_get==1 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get+ 273.15)
            output.insert('end',value)
            output.insert('end',' °K')
        
        if cb1_get==2 and cb2_get==1:
            value = (input_get-32)*5/9
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' °C')
        elif cb1_get==2 and cb2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °F')
        elif cb1_get==2 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get-32)*5/9+273.15
            output.insert('end',value)
            output.insert('end',' °K')
        
        if cb1_get==3 and cb2_get==1:
            value = (input_get-273.15)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' °C')
        elif cb1_get==3 and cb2_get==2:
            value = (input_get - 273.15) * 9/5 + 32
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' °F')
        elif cb1_get==3 and cb2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' °K')



        #create gui
    root = Tk()
    root.title('Temperature Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Temperature Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter Value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value = DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'Celsius (°C)','Fahrenheit (°F)','Kelvin (°K)',
    ] 

    cb1 = ttk.Combobox(root,values=unit_list)
    cb1.set('Celsius (°C)')
    cb1.place(x=150,y= 115)


    cb2 = ttk.Combobox(root,values=unit_list)
    cb2.set('Fahrenheit (°F)')
    cb2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 128, y =270 )
    
    
    root.mainloop()


#digital storage conver
def digital_storage_convert():
    def convert():
        
        input_get=input_value.get()
        cb1_get= cb1.get()
        cb2_get= cb2.get()
        


        if cb1_get =='Bits':
            cb1_get = 1
        elif cb1_get=='Bytes':
            cb1_get = 2
        elif cb1_get== 'Kilobytes':
            cb1_get = 3
        elif cb1_get== 'Megabytes':
            cb1_get = 4
        elif cb1_get== 'Gigabytes':
            cb1_get = 5
        elif cb1_get== 'Terabytes':
            cb1_get = 6
        elif cb1_get== 'Petabytes':
            cb1_get = 7
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb1_get)


        if cb2_get =='Bits':
            cb2_get = 1
        elif cb2_get=='Bytes':
            cb2_get = 2
        elif cb2_get== 'Kilobytes':
            cb2_get = 3
        elif cb2_get== 'Megabytes':
            cb2_get = 4
        elif cb2_get== 'Gigabytes':
            cb2_get = 5
        elif cb2_get== 'Terabytes':
            cb2_get = 6
        elif cb2_get== 'Petabytes':
            cb2_get = 7
        else:
            messagebox.showwarning('warning','"%s" is not a Unit of measurement '%cb2_get)
        

        if cb1_get==1 and cb2_get==1:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Bits')
        elif cb1_get==1 and cb2_get==2:
            value = (input_get/8)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==1 and cb2_get==3:
            output.delete(1.0,END)
            value = ((input_get/8)/(1024))
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==1 and cb2_get==4:
            output.delete(1.0,END)
            value = ((input_get/8)*0.000001 )
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==1 and cb2_get==5:
            output.delete(1.0,END)
            value = (input_get/8000000000)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==1 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/8e+12)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==1 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/ 8e+15)
            output.insert('end',value)
            output.insert('end',' Pb')


        if cb1_get==2 and cb2_get==1:
            value = (input_get*8)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==2 and cb2_get==2:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Bytes')
        elif cb1_get==2 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*0.0009765625)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==2 and cb2_get==4:
            output.delete(1.0,END)
            value = (input_get/1024/1024)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==2 and cb2_get==5:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==2 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==2 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Pb')

        if cb1_get==3 and cb2_get==1:
            value = (input_get*8192)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==3 and cb2_get==2:
            value = (input_get*1024)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==3 and cb2_get==3:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Kb')
        elif cb1_get==3 and cb2_get==4:
            output.delete(1.0,END)
            value = (input_get/1024)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==3 and cb2_get==5:
            output.delete(1.0,END)
            value = (input_get/1024/1024)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==3 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==3 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Pb')

        if cb1_get==4 and cb2_get==1:
            value = (input_get*8388608)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==4 and cb2_get==2:
            value = (input_get*1048576)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==4 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*1024)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==4 and cb2_get==4:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Mb')
        elif cb1_get==4 and cb2_get==5:
            output.delete(1.0,END)
            value = (input_get/1024)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==4 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/1024/1024)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==4 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024/1024/1024)
            output.insert('end',value)
            output.insert('end',' Pb')
        
        if cb1_get==5 and cb2_get==1:
            value = (input_get*8589934592)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==5 and cb2_get==2:
            value = (input_get*1073741824)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==5 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*1048576)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==5 and cb2_get==4:
            value = (input_get *1024)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==5 and cb2_get==5:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Gb')
        elif cb1_get==5 and cb2_get==6:
            output.delete(1.0,END)
            value = (input_get/1024)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==5 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024/1024)
            output.insert('end',value)
            output.insert('end',' Pb')

        if cb1_get==6 and cb2_get==1:
            value = (input_get*8796093022208)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==6 and cb2_get==2:
            value = (input_get*1099511627776)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==6 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*1073741824)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==6 and cb2_get==4:
            value = (input_get *1048576)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==6 and cb2_get==5:
            value = (input_get*1024)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==6 and cb2_get==6:
            output.delete(1.0,END)
            output.insert('end',input_get)
            output.insert('end',' Tb')
        elif cb1_get==6 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get/1024)
            output.insert('end',value)
            output.insert('end',' Pb')
        
        if cb1_get==7 and cb2_get==1:
            value = (input_get*9007199254740992)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bits')
        elif cb1_get==7 and cb2_get==2:
            value = (input_get*1125899906842624)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Bytes')
        elif cb1_get==7 and cb2_get==3:
            output.delete(1.0,END)
            value = (input_get*1099511627776)
            output.insert('end',value)
            output.insert('end',' Kb')
        elif cb1_get==7 and cb2_get==4:
            value = (input_get *1073741824)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Mb')
        elif cb1_get==7 and cb2_get==5:
            value = (input_get*1048576)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Gb')
        elif cb1_get==7 and cb2_get==6:
            value = (input_get*1024)
            output.delete(1.0,END)
            output.insert('end',value)
            output.insert('end',' Tb')
        elif cb1_get==7 and cb2_get==7:
            output.delete(1.0,END)
            value = (input_get)
            output.insert('end',value)
            output.insert('end',' Pb')
        


        #create gui
    root = Tk()
    root.title('Digital storage Converter')
    root.geometry('400x300')
    root.resizable(0,0)
    root.configure(bg='#68999c')

    Label(root,text='Digital storage Converter', width = '500',
        height = '2',font = ('Helvetica', 13, 'bold')).pack()
    Label(root,text='Enter Value To Convert:',
        bg = '#68999c',font = ('Helvetica', 13,)).place(x= 110,y=55)
    
    input_value = DoubleVar(root)
    Entry(root,textvariable= input_value ,width = 30).place(x= 110,y=85)
    Label(root,text='Form :',bg = '#68999c').place(x= 110,y=115)
    Label(root,text='  To :',bg = '#68999c').place(x= 110,y=145)

    unit_list = [
        'Bits','Bytes','Kilobytes','Megabytes','Gigabytes','Terabytes','Petabytes',
    ] 

    cb1 = ttk.Combobox(root,values=unit_list)
    cb1.set('Bits')
    cb1.place(x=150,y= 115)


    cb2 = ttk.Combobox(root,values=unit_list)
    cb2.set('Bytes')
    cb2.place(x=150,y= 145)
    Button(root,text='Convert',width=15,command=convert).place(x=164,y=180)

    output = Text(root,width=25,height=2,)
    output.place(x=110,y=218)
    Label(root,text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 128, y =270 )
    
    
    root.mainloop()



#create screen
screen = Tk() 
screen.geometry('200x180')
screen.title('My Converters')
screen.resizable(0,0)
screen.configure(bg='#68999c')

#create butto
m_c = Button(text='Digital Storage Converter',command=digital_storage_convert).place(x= 20, y= 20)
l_c = Button(text='       Length converter       ',command=length_converter).place(x=20,y= 50)
t_c = Button(text='  Temperature converter  ',command=time_convert).place(x=20,y= 80)
w_c = Button(text='       Weight converter       ',command=weight_converter).place(x=20,y= 110)

#create text
Label(text = 'Powered by Wadood Software',bg = '#68999c',).place(x = 20, y = 150)

screen.mainloop()