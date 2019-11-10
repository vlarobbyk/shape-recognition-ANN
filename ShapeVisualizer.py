#!/home/vlarobbyk/anaconda3/envs/ai python

__author__ = "vlarobbyk"
__copyright__ = "Grupo de Investigación en Inteligencia Artificial y Tecnologías de Asistencia"
__credits__ = ["V. Robles-Bykbaev"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "vlarobbyk"
__email__ = "vrobles@ups.edu.ec"
__status__ = "Production"


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from Utilities import Utilities

class ShapeVisualizer(tk.Frame):
    
    def __init__(self, root):
        tk.Frame.__init__(self,root)
        self.root = root
        self.utilities = Utilities()
        self.init_components()
        self.root.minsize(640,480)
        
    def init_components(self):
        entries = self.utilities.list_corpus('train/')
        sorted(entries, key = lambda str: str.split('/')[-1].split('.')[0])
        l1 = ttk.Label(self.root,text = 'Seleccione una Figura =>', font = ('Verdana',14))
        l1.grid(column = 0, row = 0)
        
        widthc, heightc = 1024, 768
        self.comboBoxShape = ttk.Combobox(self.root, values = entries, font = ('Verdana',14))
        self.comboBoxShape.grid(column = 1, row = 0, columnspan = 3)
        self.comboBoxShape.bind('<<ComboboxSelected>>', self.comboShapeSelected)
        
        self.canvas = tk.Canvas(self.root, width = widthc, height = heightc)
        self.canvas.grid(column = 0, row = 1, columnspan = 3 )
        self.canvas.configure(background = 'white')
        self.photo = ImageTk.PhotoImage(Image.open('Logo-GIIATa-small.png'))
        self.img = self.canvas.create_image(widthc/2,heightc/2, anchor = tk.CENTER,image = self.photo)
        
    def comboShapeSelected(self, event):
        print(self.comboBoxShape.get())
        image = Image.open(self.comboBoxShape.get())
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.itemconfig(self.img,image = self.photo)

if __name__=="__main__":
    root = tk.Tk()
    root.title('Shape Visualizer - UPS')
    shapev = ShapeVisualizer(root)
    root.mainloop()
    
    
    
