# Done
from tkinter import*
from tkinter import ttk
import requests


# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# API key = fc32baaa6730f67191976812c1d27dbc


def fun_call():
    state=city_name.get() # city_name ka data Get Function ke through Get kare Then State Variable mai dal di.
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+state+"&appid=fc32baaa6730f67191976812c1d27dbc").json()
    
    # Data var mai Dictionery hai osme >> "weather" ek Key hai oske andar >> List or oske andar phle means 0 no. mai "description" key hai

    wd1.config(text= data["weather"] [0] ["description"] )

    temp1.config(text= str(int(data["main"]["temp"]-273.15))) #"main" Key >> temp hai(temp in kelvin convert into celsius -273.15)
# Or int use isliye kya hai temp ko chota karne ke liye
    
    sun_rise1.config(text= data["sys"]["sunrise"]  )
    sun_set1.config(text= data["sys"]["sunset"] )
    climate1.config(text= str(data["weather"][0]["main"]) )

    #_________________________________MAIN______________________________________
win=Tk()
win.geometry("500x500") # Size of window(width x height)
win.title(" Weather REPORT ")
win.minsize(10,20)
win.config(bg="cyan")

name=Label(win,text="Weather REPORT ",
           font=("Time New Roman",30,"bold"))
name.config(bg="Yellow")
name.place(x=10,y=30,height=40,width=400)

list_state=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand",
            "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
            "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
            "Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name= StringVar() #Define Data Type of city_name 

state = ttk.Combobox(win,text="  ",values=list_state,
           font=("Time New Roman",25),textvariable=city_name) #comboBox ki value city_name mai hai
state.place(x=10,y=90,height=40,width=400)

# Display

temp=Label(win,text="Temperature : ",
      font=("Time New Roman",11,"italic"))
                # temp.config(bg="yellow") If You Want To Add Color On Text
temp.place(x=15,y=220,height=15,width=100) # Label for Temperature

temp1=Label(win,text="",
      font=("Time New Roman",11,"italic"))
temp1.place(x=115,y=220,height=15,width=100) # Label for Temperature Output

climate=Label(win,text="climate : ",
      font=("Time New Roman",11,"italic"))
climate.place(x=15,y=250,height=15,width=70) # Label for Climate

climate1=Label(win,text="",
      font=("Time New Roman",11,"italic"))
climate1.place(x=85,y=250,height=15,width=70) # Label for Climate Output

sun_rise=Label(win,text="Sunrise : ",
      font=("Time New Roman",11,"italic"))
sun_rise.place(x=15,y=280,height=15,width=70) # Label for Sunrise

sun_rise1=Label(win,text=" ",
      font=("Time New Roman",11,"italic"))
sun_rise1.place(x=85,y=280,height=15,width=70) # Label for Sunrise Output

sun_set=Label(win,text="Sunset : ",
      font=("Time New Roman",11,"italic"))
sun_set.place(x=15,y=310,height=15,width=70) # Label for sunset

sun_set1=Label(win,text=" ",
      font=("Time New Roman",11,"italic"))
sun_set1.place(x=85,y=310,height=15,width=70) # Label for sunset Output

wd=Label(win,text="Weather Description : ",
      font=("Time New Roman",11,"italic"))
wd.place(x=15,y=340,height=15,width=150) # Label for Weather Description

wd1=Label(win,text=" ",
      font=("Time New Roman",11,"italic"))
wd1.place(x=165,y=340,height=15,width=100) # Label for Weather Description Output

# BUTTON 
btn=Button(win,text=" CHECK ",
           font=("Time New Roman",30,"bold"),command=fun_call)
btn.place(x=14,y=150,height=40,width=200)

#__main__
win.mainloop()
