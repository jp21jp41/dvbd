# Color Frame Initializer
import tkinter as tk
from dig_ops import hex_to_int, digits
from math import floor

blue_hexes = {}

class colorHolder:
    def __init__(self, color):
        self.color = color
    def color_select(self, color):
        self.color = color

def color_frame(fig_prof, color_holder):
    color_frame = tk.Tk() 
    color_frame.geometry("600x400") 
    color_frame.title("Plot Color Selection")
    blue_label = tk.Label(color_frame, text = "Blue Percent")
    blue_label.grid(column = 6)
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
    color_listbox.grid(column = 6, row = 1)
    color_listbox.bind("<Double 1>", lambda x: get_selected(color_listbox, fig_prof, color_holder, color_frame))
    color_canvas.grid(column = 2, row = 2)
    
# function to select the Color Listbox value to add the canvas
def get_selected(color_listbox, fig_prof, color_holder, frame):
    try:
        color_canvas.destroy()
    except:
        pass
    for percent in color_listbox.curselection():
        if color_listbox.get(percent) == "%0.0":
            from color_canvas00 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%0.3":
            from color_canvas01 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%0.7":
            from color_canvas02 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%1.1":
            from color_canvas03 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%1.5":
            from color_canvas04 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%1.9":
            from color_canvas05 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%2.3":
            from color_canvas06 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%2.7":
            from color_canvas07 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%3.1":
            from color_canvas08 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%3.5":
            from color_canvas09 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%3.9":
            from color_canvas0A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%4.3":
            from color_canvas0B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%4.7":
            from color_canvas0C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%5.0":
            from color_canvas0D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%5.4":
            from color_canvas0E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%5.8":
            from color_canvas0F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%6.2":
            from color_canvas10 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%6.6":
            from color_canvas11 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%7.0":
            from color_canvas12 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%7.4":
            from color_canvas13 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%7.8":
            from color_canvas14 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%8.2":
            from color_canvas15 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%8.6":
            from color_canvas16 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%9.0":
            from color_canvas17 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%9.4":
            from color_canvas18 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%9.8":
            from color_canvas19 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%10.1":
            from color_canvas1A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%10.5":
            from color_canvas1B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%10.9":
            from color_canvas1C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%11.3":
            from color_canvas1D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%11.7":
            from color_canvas1E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%12.1":
            from color_canvas1F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%12.5":
            from color_canvas20 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%12.9":
            from color_canvas21 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%13.3":
            from color_canvas22 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%13.7":
            from color_canvas23 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%14.1":
            from color_canvas24 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%14.5":
            from color_canvas25 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%14.9":
            from color_canvas26 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%15.2":
            from color_canvas27 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%15.6":
            from color_canvas28 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%16.0":
            from color_canvas29 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%16.4":
            from color_canvas2A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%16.8":
            from color_canvas2B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%17.2":
            from color_canvas2C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%17.6":
            from color_canvas2D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%18.0":
            from color_canvas2E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%18.4":
            from color_canvas2F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%18.8":
            from color_canvas30 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%19.2":
            from color_canvas31 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%19.6":
            from color_canvas32 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%20.0":
            from color_canvas33 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%20.3":
            from color_canvas34 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%20.7":
            from color_canvas35 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%21.1":
            from color_canvas36 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%21.5":
            from color_canvas37 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%21.9":
            from color_canvas38 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%22.3":
            from color_canvas39 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%22.7":
            from color_canvas3A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%23.1":
            from color_canvas3B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%23.5":
            from color_canvas3C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%23.9":
            from color_canvas3D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%24.3":
            from color_canvas3E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%24.7":
            from color_canvas3F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%25.0":
            from color_canvas40 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%25.4":
            from color_canvas41 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%25.8":
            from color_canvas42 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%26.2":
            from color_canvas43 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%26.6":
            from color_canvas44 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%27.0":
            from color_canvas45 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%27.4":
            from color_canvas46 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%27.8":
            from color_canvas47 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%28.2":
            from color_canvas48 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%28.6":
            from color_canvas49 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%29.0":
            from color_canvas4A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%29.4":
            from color_canvas4B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%29.8":
            from color_canvas4C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%30.1":
            from color_canvas4D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%30.5":
            from color_canvas4E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%30.9":
            from color_canvas4F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%31.3":
            from color_canvas50 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%31.7":
            from color_canvas51 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%32.1":
            from color_canvas52 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%32.5":
            from color_canvas53 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%32.9":
            from color_canvas54 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%33.3":
            from color_canvas55 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%33.7":
            from color_canvas56 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%34.1":
            from color_canvas57 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%34.5":
            from color_canvas58 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%34.9":
            from color_canvas59 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%35.2":
            from color_canvas5A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%35.6":
            from color_canvas5B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%36.0":
            from color_canvas5C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%36.4":
            from color_canvas5D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%36.8":
            from color_canvas5E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%37.2":
            from color_canvas5F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%37.6":
            from color_canvas60 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%38.0":
            from color_canvas61 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%38.4":
            from color_canvas62 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%38.8":
            from color_canvas63 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%39.2":
            from color_canvas64 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%39.6":
            from color_canvas65 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%40.0":
            from color_canvas66 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%40.3":
            from color_canvas67 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%40.7":
            from color_canvas68 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%41.1":
            from color_canvas69 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%41.5":
            from color_canvas6A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%41.9":
            from color_canvas6B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%42.3":
            from color_canvas6C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%42.7":
            from color_canvas6D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%43.1":
            from color_canvas6E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%43.5":
            from color_canvas6F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%43.9":
            from color_canvas70 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%44.3":
            from color_canvas71 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%44.7":
            from color_canvas72 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%45.0":
            from color_canvas73 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%45.4":
            from color_canvas74 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%45.8":
            from color_canvas75 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%46.2":
            from color_canvas76 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%46.6":
            from color_canvas77 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%47.0":
            from color_canvas78 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%47.4":
            from color_canvas79 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%47.8":
            from color_canvas7A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%48.2":
            from color_canvas7B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%48.6":
            from color_canvas7C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%49.0":
            from color_canvas7D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%49.4":
            from color_canvas7E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%49.8":
            from color_canvas7F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%50.1":
            from color_canvas80 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%50.5":
            from color_canvas81 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%50.9":
            from color_canvas81 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%51.3":
            from color_canvas82 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%51.7":
            from color_canvas83 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%52.1":
            from color_canvas84 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%52.5":
            from color_canvas85 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%52.9":
            from color_canvas86 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%53.3":
            from color_canvas87 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%53.7":
            from color_canvas88 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%54.1":
            from color_canvas89 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%54.5":
            from color_canvas8A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%54.9":
            from color_canvas8B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%55.2":
            from color_canvas8C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%55.6":
            from color_canvas8D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%56.0":
            from color_canvas8E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%56.4":
            from color_canvas8F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%56.8":
            from color_canvas90 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%57.2":
            from color_canvas92 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%57.6":
            from color_canvas93 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%58.0":
            from color_canvas94 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%58.4":
            from color_canvas95 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%58.8":
            from color_canvas96 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%59.2":
            from color_canvas97 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%59.6":
            from color_canvas98 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%60.0":
            from color_canvas99 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%60.3":
            from color_canvas9A import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%60.7":
            from color_canvas9B import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%61.1":
            from color_canvas9C import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%61.5":
            from color_canvas9D import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%61.9":
            from color_canvas9E import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%62.3":
            from color_canvas9F import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%62.7":
            from color_canvasA0 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%63.1":
            from color_canvasA1 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%63.5":
            from color_canvasA2 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%63.9":
            from color_canvasA3 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%64.3":
            from color_canvasA4 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%64.7":
            from color_canvasA5 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%65.0":
            from color_canvasA6 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%65.4":
            from color_canvasA7 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%65.8":
            from color_canvasA8 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%66.2":
            from color_canvasA9 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%66.6":
            from color_canvasAA import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%67.0":
            from color_canvasAB import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%67.4":
            from color_canvasAC import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%67.8":
            from color_canvasAD import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%68.2":
            from color_canvasAE import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%68.6":
            from color_canvasAF import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%69.0":
            from color_canvasB0 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%69.4":
            from color_canvasB1 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%69.8":
            from color_canvasB2 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%70.1":
            from color_canvasB3 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%70.5":
            from color_canvasB4 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%70.9":
            from color_canvasB5 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%71.3":
            from color_canvasB6 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%71.7":
            from color_canvasB7 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%72.1":
            from color_canvasB8 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%72.5":
            from color_canvasB9 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%72.9":
            from color_canvasBA import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%73.3":
            from color_canvasBB import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%73.7":
            from color_canvasBC import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%74.1":
            from color_canvasBD import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%74.5":
            from color_canvasBE import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%74.9":
            from color_canvasBF import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%75.2":
            from color_canvasC0 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%75.6":
            from color_canvasC1 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%76.0":
            from color_canvasC2 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%76.4":
            from color_canvasC3 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%76.8":
            from color_canvasC4 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%77.2":
            from color_canvasC5 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%77.6":
            from color_canvasC6 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%78.0":
            from color_canvasC7 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%78.4":
            from color_canvasC8 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%78.8":
            from color_canvasC9 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%79.2":
            from color_canvasCA import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%79.6":
            from color_canvasCB import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%80.0":
            from color_canvasCC import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%80.3":
            from color_canvasCD import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%80.7":
            from color_canvasCE import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%81.1":
            from color_canvasCF import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%81.5":
            from color_canvasD0 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%81.9":
            from color_canvasD1 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%82.3":
            from color_canvasD2 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%82.7":
            from color_canvasD3 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%83.1":
            from color_canvasD4 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%83.5":
            from color_canvasD5 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%83.9":
            from color_canvasD6 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%84.3":
            from color_canvasD7 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%84.7":
            from color_canvasD8 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%85.0":
            from color_canvasD9 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%85.4":
            from color_canvasDA import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%85.8":
            from color_canvasDB import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%86.2":
            from color_canvasDC import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%86.6":
            from color_canvasDD import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%87.0":
            from color_canvasDE import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%87.4":
            from color_canvasDF import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%87.8":
            from color_canvasE0 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%88.2":
            from color_canvasE1 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%88.6":
            from color_canvasE2 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%89.0":
            from color_canvasE3 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%89.4":
            from color_canvasE4 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%89.8":
            from color_canvasE5 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%90.1":
            from color_canvasE6 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%90.5":
            from color_canvasE7 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%90.9":
            from color_canvasE8 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%91.3":
            from color_canvasE9 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%91.7":
            from color_canvasEA import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%92.1":
            from color_canvasEB import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%92.5":
            from color_canvasEC import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%92.9":
            from color_canvasED import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%93.3":
            from color_canvasEE import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%93.7":
            from color_canvasEF import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%94.1":
            from color_canvasF0 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%94.5":
            from color_canvasF1 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%94.9":
            from color_canvasF2 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%95.2":
            from color_canvasF3 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%95.6":
            from color_canvasF4 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%96.0":
            from color_canvasF5 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%96.4":
            from color_canvasF6 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%96.8":
            from color_canvasF7 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%97.2":
            from color_canvasF8 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%97.6":
            from color_canvasF9 import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%98.0":
            from color_canvasFA import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%98.4":
            from color_canvasFB import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%98.8":
            from color_canvasFC import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%99.2":
            from color_canvasFD import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%99.6":
            from color_canvasFE import color_canvas
            color_canvas(fig_prof, color_holder, frame)
        if color_listbox.get(percent) == "%100.0":
            from color_canvasFF import color_canvas
            color_canvas(fig_prof, color_holder, frame)