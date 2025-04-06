# Data Visualization Backend Designer (DVBD)
# Justin Pizano

# Import Libraries
import os
import sys
import pandas as pnd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
from scipy import stats
from tkinter.filedialog import askopenfilename

# Modules "inputter", "color_frame", and "dig_ops" can be found on GitHub through jp21jp41
import inputter
from dig_ops import *
from color_frame_init import color_frame, colorHolder
from doc_frame_init import *



# figureProfile class works with graphical user interfaces that allow plots
# to be added and changed.
class figureProfile:
    # initializer
    def __init__(self, data, row_names = ""):
        self.data = [data]
        print(self.data[0])
        try:
            if not row_names.equals(""):
                print('55')
                self.row_names = row_names
        except:
            if row_names != "":
                print('54')
                self.row_names = row_names
        try:
            self.data_columns.append(data.name)
        except:
            try:
                self.data_columns = data.name
            except:
                try:
                    self.data_columns = data.columns
                except:
                    pass
        self.forget_choices = False
        self.horiz = False
        self.filler = 0
        self.color = "g"
        self.background_color = "white"
        self.basic_colors = ["Green", "Red", "Blue"]
        self.color_options = ["Green", "Blue", "Red", "Other"]
        self.label = False
        self.base_canvas = False
    
    def quickColorMenu(self, text, holder, x_value, y_value):
        choice = tk.StringVar(self.frame)
        choice.set(text)
        menu = tk.OptionMenu(self.frame, choice,
                                   *self.color_options, command = lambda x : self.basic_color(x, holder))
        menu.place(x = x_value, y = y_value)
        return menu
    
    
    # function to change out the data set
    def data_edit(self, data):
        self.data = [data]
    
    # function to select the Tkinter frame
    def put_frame(self, frame):
        self.frame = frame
    
    # function to change or keep the choice menu
    def choice_menu_set(self, choices, choice_quote, same):
        # No choices i.e. no choice_menu
        if choices == 0:
            # Forget the choices at hand if they are there
            if self.forget_choices:
                # If there were no choices to begin with (the same set, no option menu), nothing needs to be destroyed
                if same:
                    return
                # If there were choices to begin with, the menu needs to be destroyed
                else:
                    self.choice_menu.destroy()
                    return
            # Nothing to forget
            else:
                return
        # There are choices to forget
        if self.forget_choices:
            # Same previous choices, no changes to be made
            if same:
                return
            # Different choice menu, destroy and recurse to add new menu
            else:
                self.choice_menu.destroy()
                self.forget_choices = False
                self.choice_menu_set(choices, choice_quote, same)
        # There are choices to be added with no choices to forget
        else:
            self.forget_choices = True
            choice_str = tk.StringVar(self.frame)
            choice_str.set(choice_quote)
            choice_menu = tk.OptionMenu(self.frame, choice_str, *choices)
            choice_menu.place(y = 650)
            self.choice_menu = choice_menu
    
    # function to add the canvas
    def canvas_set(self, base_made = False):
        # Leave the canvas as is if there was one to begin with
        if self.base_canvas == True:
            pass
        else:
            try:
                inputter.list_destroyer(self.base_asset_list)
            except:
                pass
            # Add a flip axis button
            flip_button = tk.Button(self.frame, text= "Flip Axis", 
                              command = lambda : self.flip()) 
            flip_button.place(x = 600) 
            # Add a button to save the figure
            save_button = tk.Button(self.frame, text = "Save Figure", 
                                    command = lambda : self.save())
            save_button.place(x = 600, y = 30)
            upload_options = tk.Button(self.frame, text = "Upload Options",
                                       command = lambda : doc_frame(self))
            upload_options.place(x = 600, y = 100)
            # Add a button to add label axes
            label_button = tk.Button(self.frame, text = "Label (Pre-alpha)",
                                     command = lambda : self.toggle_label())
            label_button.place(x = 670)
            # Add a color option menu
            color_choice = tk.StringVar(self.frame)
            color_choice.set("Select Color")
            self.init_holder = colorHolder(self.color)
            color_menu = tk.OptionMenu(self.frame, color_choice,
                                       *self.color_options, command = lambda x : self.basic_color(x, self.init_holder))
            color_menu.place(x = 600, y = 60)
            bg_color_choice = tk.StringVar(self.frame)
            bg_color_choice.set("Select Background Color")
            self.bg_holder = colorHolder(self.background_color)
            bg_menu = tk.OptionMenu(self.frame, bg_color_choice,
                                       *self.color_options, command = lambda x : self.basic_color(x, self.bg_holder))
            bg_menu.place(x = 700, y = 60)
            self.base_asset_list = flip_button, save_button, upload_options, label_button, color_menu, bg_menu
            self.base_canvas = True
        # Destroy current matplotlib integrated canvas widget if there was one
        try:
            self.frame.current_canvas_widget.destroy()
        except:
            pass
        # Add current matplotlib integrated canvas widget
        self.initial_img = Figure(figsize=(5, 4), dpi = 100) 
        self.ax = self.initial_img.add_subplot(111) 
        self.canvas = FigureCanvasTkAgg(self.initial_img, master= self.frame) 
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x = 0, y = 50)
        self.current_canvas_widget = self.canvas.get_tk_widget()
    
    # Basic color function
    def basic_color(self, color, holder):
        # Add one of the basic colors or allow the separate frame selection
        if color in self.basic_colors:
            self.color_select(color, holder)
        else:
            color_frame(self, holder)
    
    # Select a color
    def color_select(self, fill_color, holder):
        holder.color = fill_color
        self.basic_plot(self.plot_type)
    
    # function to change the orientation variable
    def flip(self):
        if self.horiz == False:
            self.horiz = True
        else:
            self.horiz = False
        self.basic_plot(self.plot_type)
    
    # function to toggle labels
    def toggle_label(self):
        if self.label == False:
            self.label = True
        else:
            self.label = False
    # function to toggle animation (not yet implemented)
    def toggle_animation(self):
        if self.animated == False:
            self.animated = True
        else:
            self.animated = False
        
    # function to save plot with incrementer to store different figures
    def save(self):
        self.initial_img.savefig(os.getcwd() + "\\" + str(self.filler))
        self.filler += 1
    
    # function to plot onto the GUI
    def basic_plot(self, plot_type):
        try:
            list_destroyer(self.basic_plot_assets)
        except:
            pass
        # Set canvas
        self.canvas_set()
        # Same parameter try-except based on plot type
        try:
            # If statement: It's either the same or not
            if self.plot_type == plot_type:
                same = True
            else:
                self.plot_type = plot_type
                same = False
        # Except: The assumption is there is not a plot type yet and therefore it cannot be the same
        except:
            self.plot_type = plot_type
            same = False
        # Histogram case
        if self.plot_type == "Histogram":
            print(self.data)
            # Histogram counts and bins
            hist_counts, hist_bins = np.histogram(self.data[0])
            # Matplotlib stairs
            plt.stairs(hist_counts, hist_bins)
            # Horizontal or Vertical Histogram based on set orientation
            if self.horiz:
                self.ax.hist(hist_bins[:-1], hist_bins, weights= hist_counts, 
                        orientation = "horizontal", color = self.init_holder.color) 
            else: 
                self.ax.hist(hist_bins[:-1], hist_bins, weights= hist_counts, 
                        color = self.init_holder.color)
            # No choice menu set (must be ran if it has to be deleted)
            self.choice_menu_set(0, "", same)
        # Bar Graph
        elif self.plot_type == "Bar Graph":
            # Orientation-based plot
            if self.horiz:
                self.ax.barh(self.data[0], 
                             max(self.data[0]), color = self.init_holder.color)
            else:
                self.ax.bar(self.data[0], 
                            max(self.data[0]), color = self.init_holder.color)
            # List of new choices and choice menu set added
            choices = ["Original", "Labeled", "Stacked", "Grouped", "Hat", 
                       "Bar of Pie", "Nested Pie", "Polar Axis"]
            self.choice_menu_set(choices, "Select a type of bar graph", same)
        # Boxplot
        elif self.plot_type == "Boxplot":
            # Style
            plt.style.use('_mpl-gallery')
            # Orientation-based plot
            if self.horiz:
                self.ax.boxplot(self.data[0], widths=1.5, vert= False)
            else:
                self.ax.boxplot(self.data[0], widths=1.5)
            # Choice menu set function
            self.choice_menu_set(0, "", same)
        # Distribution plot (no set horizontal)
        elif self.plot_type == "Distribution":
            if self.horiz:
                pass
            else:
                self.ax.plot(self.data[0], color = self.init_holder.color)
            self.choice_menu_set(0, "", same)
        # Pie chart (minimally functional)
        elif self.plot_type == "Pie (Pre-alpha)":
            """
            sys.setrecursionlimit((len(self.data[0]) + 20)*100)
            coords = [(0.5, 0.5)]
            sum = 0
            for item in self.data[0]:
                sum += item
            pie = CoordCircle(coords, sum)
            pie.coord_circle(self.data[0], self.ax, self.init_holder.color)
            sys.setrecursionlimit(1000)
            """
            self.ax.pie(self.data[0], colors = [hex_to_rgba(self.color) for x in self.data[0]])
        elif self.plot_type == "Table (Pre-alpha)":
            self.ax.table(pnd.DataFrame(self.data[0]))
        elif self.plot_type == "Regression":
            res = stats.linregress(self.data[0], self.row_names)
            try:
                if self.label:
                    self.ax.plot(self.data[0], self.row_names, 'o', label = self.row_names,
                                 color = self.dot_holder.color)
                    self.ax.plot(self.data[0], res.intercept + res.slope*self.data[0], 
                                 'r', label = self.row_names, color = self.line_holder.color)
                    try:
                        self.color_menu.destroy()
                    except:
                        pass
                else:
                    self.ax.plot(self.data[0], self.row_names, 'o', color = self.dot_holder.color)
                    self.ax.plot(self.data[0], res.intercept + res.slope*self.data[0], 
                                 'r', color = self.line_holder.color)
                dot_color_menu = self.quickColorMenu("Select Dot Color", self.dot_holder, 600, 60)
                line_color_menu = self.quickColorMenu("Select Line Color", self.line_holder, 750, 60)
                self.reg_plots = True
                
                self.base_asset_list[4].destroy()
                self.base_asset_list[5].destroy()
                self.base_asset_list[0].place_forget()
                self.basic_plot_assets = dot_color_menu, line_color_menu
                self.base_canvas = False
            except:
                self.dot_holder = colorHolder('b')
                self.line_holder = colorHolder('r')
                self.basic_plot(plot_type)
                
        elif self.plot_type == "Extra (Pre-alpha)": 
            patch_set = []
            polygon = Polygon(np.random.rand(10, 2), closed=True)
            patch_set.append(polygon)
            p = PatchCollection(patch_set, alpha=0.4)
            self.ax.add_collection(p)
        self.ax.set_facecolor(self.bg_holder.color)
        
    
# Run the backend designer
def run(asker, fmt):
    print("33")
    if fmt == 0:
        file_exp = tk.Tk()
        directory = askopenfilename(initialdir = "/", title = "Select File")
        asker.basic_read(init_input = directory, no_inputter = True)
    if fmt == 1:
        # Function call to read a data file
        asker.basic_read(str_statement = "Please enter the name" + 
                                " of the file to use")
    
    
    
    # Column selection function call
    try:
        print("Here are the column choices: " + 
              str([x.name for x in asker.data]))
    except:
        print("Here are the column choices:" +
              str([x for x in asker.data]))
    asker.basic_read(str_statement = "Please select the column you" +
                            " seek to visualize data from.", readtype = "column")
    
    # figureProfile Object
    figs_saved = figureProfile(asker.current_column, asker.row_names)
    # Return the figureProfile Object
    return(figs_saved)

# Tkinter mainloop for backend designer
def mainloop(figure_profile, asker):
    # Plot types
    plot_types = ["Histogram", "Bar Graph", "Boxplot", "Distribution", "Pie (Pre-alpha)", 
                  "Table (Pre-alpha)", "Extra (Pre-alpha)", "Regression"]
    # While-loop base case
    not_finished = True
    # A while-loop that is supposed to
    # start the designer, allowing continuation
    # if the user closes the window and
    # wants to continue
    while not_finished:
        frame = tk.Tk()
        figure_profile.put_frame(frame)
        frame.geometry("900x550")
        plot_choice = tk.StringVar(frame)
        plot_choice.set("Plot Type")
        plot_menu = tk.OptionMenu(frame, plot_choice, *plot_types,
                                  command= lambda x : figure_profile.basic_plot(x))
        plot_menu.place(x = 0)
        full_exit = tk.Button(frame, text= "Exit", command= lambda: inputter.full_exit())
        full_exit.place(x = 850, y = 0)
        frame.title("Data Visualization Backend Designer")
        frame.mainloop()
        not_finished = asker.basic_ask(
            "Are you finished selecting visuals?")
        
        
        
    sys.exit()


"""
# Initial asker object
asker = inputter.adv_inputters()
# Running backend designer
x = run(asker)
# Backend designer mainloop
mainloop(x, asker)
"""


