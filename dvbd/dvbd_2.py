# Data Visualization Backend Designer (DVBD)
# Justin Pizano

# Import Libraries
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
import matplotlib.colors as pltcolors

# Modules "inputter", "color_frame", and "dig_ops" can be found on GitHub through jp21jp41
import inputter
from dig_ops import *
from color_frame_init import color_frame


# figureProfile class works with graphical user interfaces that allow plots
# to be added and changed.
class figureProfile:
    # initializer
    def __init__(self, data):
        self.data = [data]
        self.has_canvas = False
        self.forget_choices = False
        self.horiz = False
        self.filler = 0
        self.color = "g"
        self.basic_colors = ["Green", "Red", "Blue"]
        
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
            choice_menu.grid()
            self.choice_menu = choice_menu
    
    # function to add the canvas
    def canvas_set(self):
        # Leave the canvas as is if there was one to begin with
        if self.has_canvas:
            pass
        else:
            # Canvas has-a attribute set to true
            self.has_canvas = True
            # Add a flip axis button
            flip_button = tk.Button(self.frame, text= "Flip Axis", 
                              command = lambda : self.flip()) 
            flip_button.grid(column = 1) 
            # Add a button to save the figure
            save_button = tk.Button(self.frame, text= "Save Figure", 
                                    command = lambda : self.save())
            save_button.grid(column = 2, row = 1)
            # Add a color option menu
            color_choice = tk.StringVar(self.frame)
            color_choice.set("Select Color")
            color_options = ["Green", "Blue", "Red", "Other"]
            color_menu = tk.OptionMenu(self.frame, color_choice,
                                       *color_options, command = lambda x : self.basic_color(x))
            color_menu.grid()
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
        self.canvas.get_tk_widget().grid(row = 1)
        self.current_canvas_widget = self.canvas.get_tk_widget()
    
    # Basic color function
    def basic_color(self, color):
        # Add one of the basic colors or allow the separate frame selection
        if color in self.basic_colors:
            self.color_select(color)
        else:
            color_frame(self)
    
    # Select a color
    def color_select(self, fill_color):
        self.color = fill_color
        self.basic_plot(self.plot_type)
    
    # function to change the orientation variable
    def flip(self):
        if self.horiz == False:
            self.horiz = True
        else:
            self.horiz = False
        self.basic_plot(self.plot_type)
    
    # function to toggle animation (not yet implemented)
    def toggle_animation(self):
        if self.animated == False:
            self.animated = True
        else:
            self.animated = False
        
    # function to save plot with incrementer to store different figures
    def save(self):
        self.initial_img.savefig(os.getcwd() + str(self.filler))
        self.filler += 1
    
    # function to plot onto the GUI
    def basic_plot(self, plot_type):
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
            # Histogram counts and bins
            hist_counts, hist_bins = np.histogram(self.data[0])
            # Matplotlib stairs
            plt.stairs(hist_counts, hist_bins)
            # Horizontal or Vertical Histogram based on set orientation
            if self.horiz:
                self.ax.hist(hist_bins[:-1], hist_bins, weights= hist_counts, 
                        orientation = "horizontal", color = self.color) 
            else: 
                self.ax.hist(hist_bins[:-1], hist_bins, weights= hist_counts, 
                        color = self.color)
            # No choice menu set (must be ran if it has to be deleted)
            self.choice_menu_set(0, "", same)
        # Bar Graph
        elif self.plot_type == "Bar Graph":
            # Orientation-based plot
            if self.horiz:
                self.ax.barh(self.data[0], 
                             max(self.data[0]), color = self.color)
            else:
                self.ax.bar(self.data[0], 
                            max(self.data[0]), color = self.color)
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
                self.ax.plot(self.data[0], color = self.color)
            self.choice_menu_set(0, "", same)
        # Pie chart (minimally functional)
        elif self.plot_type == "Pie":
            self.ax.pie(self.data[0], colors = [hex_to_rgba(self.color)])
            
            
        
    
# Run the backend designer
def run(asker):
    
    # Function call to read a data file
    asker.basic_read(str_statement = "Please enter the name" + 
                            " of the file to use")
    
    
    
    # Column selection function call
    print("Here are the column choices: " + 
          str([x.name for x in asker.data]))
    asker.basic_read(str_statement = "Please select the column you" +
                            " seek to visualize data from.", readtype = "column")
    
    
    # figureProfile Object
    figs_saved = figureProfile(asker.current_column)
    # Return the figureProfile Object
    return(figs_saved)

# Tkinter mainloop for backend designer
def mainloop(figure_profile, asker):
    # Plot types
    plot_types = ["Histogram", "Bar Graph", "Boxplot", "Distribution", "Pie"]
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
        plot_menu.grid()
        frame.title("Data Visualization Backend Designer")
        frame.mainloop()
        not_finished = asker.basic_ask(
            "Are you finished selecting visuals?")
        
        
        
    sys.exit()


# Initial asker object
asker = inputter.adv_inputters()
# Running backend designer
x = run(asker)
# Backend designer mainloop
mainloop(x, asker)



# Made with the help of various API reference pages such as those of
# Matplotlib, Pandas, Numpy, and Tkinter

