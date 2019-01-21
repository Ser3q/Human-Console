from tkinter import *
import api


class Application(Frame):
    """GUI for my ASR program"""

    def __init__(self, master):
        """Init the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Create label and button"""
        self.label = Label(self, text="Naciśnij przycisk, by rozpocząć rozpoznawanie głosu.", relief="solid")
        self.label.grid()
        self.button = Button(self, text="Start", width=15, height=3)
        self.button["command"]= self.Start
        self.button.grid()


    def Start(self):
        api.run()

root = Tk()
root.title("ASR Ludzka Konsola ver. 1.0.0 Alpha")
root.geometry("290x80")

app = Application(root)
root.mainloop()
