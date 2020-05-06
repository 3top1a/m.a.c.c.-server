import tkinter as tk
import threading
import os

class GUI(threading.Thread):

    Main = None

    DataLabel = None
    LeftDataReadouts = None
    RightDataSending = None
    DataFrame = None
    DataEntry = None
    DataSendButton = None
    LeftAreaFrame = None

    def __init__(self, _main):
        self.Main = _main
        threading.Thread.__init__(self)
        self.start()

    def QuitCallback(self):
        os._exit(os.EX_OK)
    
    def run(self):
        self.root = tk.Tk()
        self.root.title("AutoMa Craft Controller")
        self.root.minsize(100, 100)
        self.root.protocol("WM_DELETE_WINDOW", self.QuitCallback)

        #Left frame
        self.LeftAreaFrame = tk.Frame(self.root, bg='#333', width=500)
        self.LeftAreaFrame.pack(expand=True, fill='both', side='left')

        #Left Data Readouts
        self.DataLabel = tk.Label(self.LeftAreaFrame, text="yeet", height="20", width="40", justify=tk.LEFT, anchor="nw")
        self.DataLabel.pack()

        #Data sending frame
        self.DataFrame = tk.Frame(self.root, width=100, bg='white', height=200, relief='sunken', borderwidth=2)
        self.DataFrame.pack(expand=True, fill='both', side='right', anchor='s')

        def send():
            self.Main.Agents[0].send(".toggle freecam")
            
        
        #Button and entry
        self.DataEntry = tk.Entry(self.DataFrame)
        self.DataEntry.insert(1, ". toggle freecam")
        self.DataEntry.pack(side=tk.LEFT)
        
        self.DataSendButton = tk.Button(self.DataFrame, text="Send command", command = send)
        self.DataSendButton.pack(side=tk.RIGHT, pady=20)

        def update():
            to = str( self.Main.Agents[0].DataString() )

            self.ChangeDatalabel(to)
            self.root.after(50, update)

        self.root.after(50, update)
        self.root.mainloop()
    
    def ChangeDatalabel(self, text):
        if(self.DataLabel != None):
            self.DataLabel.config(text=text)