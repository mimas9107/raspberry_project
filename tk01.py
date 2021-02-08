import tkinter as tk

class Window(tk.Tk): ## this class inherit from tk.Tk 
    def __init__(self):
        super().__init__()
        self.title(" Tk window hello world!")
        
        lbl = tk.Label(self,text = "Tk window hello world!\n")
        lbl.pack(fill=tk.BOTH, expand=True, padx=100, pady=100)
        
        btn = tk.Button(self,text = "click me!\n",command=self.btn_command)
        btn.pack(side=left)
        
        btn2 = tk.Button(self, text = "ahahahahahaha\n", command=self.btn_command2)
        btn2.pack(side=right)
    def btn_command(self):
        print("exec btn command")
    def btn_command2(self):
        print("hahahahahahaha")


## The main entry point: it's presented this file being called directly.
if __name__ == "__main__": 
    ## create a instance object celled 'window'
    window=Window() 
    ## After the instance been created, the mainloop method can be executed.
    window.mainloop()      
