from gpiozero import MCP3008
import time
import tkinter as tk

class Application(tk.Frame): ## this class inherit from tk.Tk 
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.lbltemp = tk.Label(self,text = "Temperature: ")
        self.lbltemp.grid(row=0, column=0)
        self.lbltemp_answer = tk.Label(self)
        self.lbltemp_answer.grid(row=0, column=1)

        self.lbllumin = tk.Label(self,text = "Luminance: ")
        self.lbllumin.grid(row=1, column=0)
        self.lbllumin_answer = tk.Label(self)
        self.lbllumin_answer.grid(row=1, column=1)
        
        self.btn_detectio = tk.Button(self,text = "Start detecting", command=self.detectio_loop)
        self.btn_detectio.grid(row=2, column=0)
        self.btn = tk.Button(self,text = "QUIT\n",command=self.btn_command)
        self.btn.grid(row=2,column=1)
        
        self.pack()
        self.flag_detectio = True
        
    def btn_command(self):
        print("exec btn command")
        self.flag_detectio = False
        self.master.destroy()

    def detectio_loop(self):
        # while True:
            temp= self.get_temperature()
            
            self.lbltemp_answer.config(text=temp)
            self.lbltemp_answer.grid(row=0, column=1)
            
            lumin= self.get_luminance()
            self.lbllumin_answer.config(text=lumin)
            self.lbllumin_answer.grid(row=1, column=1)
            

            # time.sleep(1)
            # if self.flag_detectio:
            #     continue
            # else:
            #     break


    def get_luminance(self):
        light=0
        lightness = MCP3008(7)
        for i in range(1,6):
            valuel = lightness.value
            light = light + valuel
            time.sleep(0.05)
        light = light/5

        print('lumin: ',light*100)
        # time.sleep(1)
        return light*100

    def get_temperature(self):
        temp=0
        lm35 = MCP3008(6)
        for i in range(1,6):
            value = lm35.value
            temp = temp + value
            time.sleep(0.05)
        temp = temp/5    
        print('temperature: ',temp*3.3*100)

# def main():
#     lm35 = MCP3008(0)
#     lightness = MCP3008(7)
#     temp=0
#     light=0
#     while True:
#         for i in range(1,6):
#             value = lm35.value
#             temp = temp + value
#             time.sleep(0.05)
#         temp = temp/5    
        
#         print('temperature: ',temp*3.3*100)
        
#         for i in range(1,6):
#             valuel = lightness.value
#             light = light + valuel
#             time.sleep(0.05)
#         light = light/5
#         print('lumin: ',light*100)
#         time.sleep(1)
#         temp = 0
#         light = 0
    
def main():
    window = tk.Tk()
    window.geometry("240x140+0+0")
    window.title(" 溫度 & 照度 類比偵測轉數位 via MCP3008 晶片")
    
    app = Application(master=window)
    
    
    
    app.mainloop()

if __name__ == '__main__':
    main()  # 或是任何你想執行的函式
