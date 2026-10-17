# # digital clock
import tkinter
from  time import strftime
clocker=tkinter.Tk()
clocker.title("Digital clock")
def clocker_time():
    time = strftime("%H:%M:%S %p \n %d|%m|%y")
    design_clocker.config(text=time)
    design_clocker.after(1000,clocker_time)
design_clocker = tkinter.Label(clocker, font=("Hoedown", 40), bg="light blue", fg="gray")
design_clocker.pack(anchor='center')
clocker_time()
clocker.mainloop()