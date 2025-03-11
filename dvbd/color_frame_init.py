# Color Frame Initializer
import tkinter as tk
from dig_ops import hex_to_int, digits
from math import floor
from runpy import run_module

blue_hexes = {}

def color_frame(fig_prof):
    color_frame = tk.Tk() 
    color_frame.geometry("600x400") 
    color_frame.title("Plot Color Selection")
    color_listbox = tk.Listbox(color_frame)
    color_canvas = tk.Canvas(color_frame, width = 320, height = 320)
    hex_strings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "A", "B", "C", "D", "E", "F"] 
    # Loop over strings, create selectable values
    for str1 in hex_strings: 
        for str2 in hex_strings:
            integer = hex_to_int(str1 + str2)
            str_int = digits(integer, 2)
            blue_percent = "%" + str((floor(integer * 1000/255)/10))
            blue_hexes.update({blue_percent : "color_canvas" + str_int})
            color_listbox.insert(integer, blue_percent)
            
    # Grid the listbox
    color_listbox.grid(column = 7)
    color_listbox.bind("<Double 1>", lambda x: get_selected(color_listbox, fig_prof, color_frame))
    color_canvas.grid(column = 2, row = 2)
    
# function to select the Color Listbox value to add the canvas
def get_selected(color_listbox, fig_prof, frame):
    for percent in color_listbox.curselection():
        print(color_listbox.get(percent))
        if color_listbox.get(percent) == "%0.0":
            import color_canvas00
            color_canvas00.color_canvas00(fig_prof, frame)
        if color_listbox.get(percent) == "%100.0":
            import color_canvasFF
            color_canvasFF.color_canvasFF(fig_prof, frame)