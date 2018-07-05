#cd D:\Diego\Documents\GitHub\CubeWorld-equipment-simulator
#python equipmentsimulator.py

from tkinter import *
from tkinter import ttk

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.createWidgets()
        self.title("CW equipmentsimulator")
    def createWidgets(self):
        selectedEquipmentFrame = ttk.Frame(self, padding="3 3 0 12")
        selectedEquipmentFrame.grid(column=1, row=1, sticky=(N, W, E, S))
        selectionFrame = ttk.Frame(self, padding="3 0 12 12", width=200)
        selectionFrame.grid(column=2, row=1, sticky=(N, W, E, S))

        selectedEquipmentFrame.columnconfigure(1, weight=1)
        selectedEquipmentFrame.columnconfigure(2, weight=1)
        selectedEquipmentFrame.rowconfigure(1, weight=1)
        selectedEquipmentFrame.rowconfigure(2, weight=1)
        selectedEquipmentFrame.rowconfigure(3, weight=1)
        selectedEquipmentFrame.rowconfigure(4, weight=1)
        selectedEquipmentFrame.rowconfigure(5, weight=1)
        selectedEquipmentFrame.rowconfigure(6, weight=1)

        ttk.Button(selectedEquipmentFrame, text="left weapon").grid(column=1, row=1, sticky=(N, W, E, S), padx=(0, 50), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="left ring").grid(column=1, row=2, sticky=(N, W, E, S), padx=(0, 50), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="neck").grid(column=1, row=3, sticky=(N, W, E, S), padx=(0, 50), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="chest").grid(column=1, row=4, sticky=(N, W, E, S), padx=(0, 50), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="feet").grid(column=1, row=5, sticky=(N, W, E, S), padx=(0, 50), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="special").grid(column=1, row=6, sticky=(N, W, E, S), padx=(0, 50), pady=(0, 10))

        ttk.Button(selectedEquipmentFrame, text="right weapon").grid(column=2, row=1, sticky=(N, W, E, S), padx=(50, 0), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="right ring").grid(column=2, row=2, sticky=(N, W, E, S), padx=(50, 0), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="shoulder").grid(column=2, row=3, sticky=(N, W, E, S), padx=(50, 0), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="hands").grid(column=2, row=4, sticky=(N, W, E, S), padx=(50, 0), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="light").grid(column=2, row=5, sticky=(N, W, E, S), padx=(50, 0), pady=(0, 10))
        ttk.Button(selectedEquipmentFrame, text="pet").grid(column=2, row=6, sticky=(N, W, E, S), padx=(50, 0), pady=(0, 10))

        def printInfo():#prints window size
            print(self.winfo_width(), self.winfo_height())

root = Application()
root.mainloop()
