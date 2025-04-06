# Backend Designer Initializer (GUI)
import tkinter as tk
import pandas as pnd
import inputter
from dvbd_2 import *

class MultiData():
    def __init__(self, tkwindow, asker, count = 1, final_count = 2):
        self.tkwindow = tkwindow
        self.asker = asker
        self.label_opt_set = {}
        self.row_assets = {}
        self.columns = []
        self.value_index = {}
        self.total = {}
        self.count = count
        self.final_count = final_count
        self.current_values = []
        self.all_values = {}
        self.data = []
        self.true_data = {}
        self.data_edit = {}
        self.submit_check = []
        self.name_hierarchy = {}
        self.count_menu = ['Row Names', 'Columns']
    
    def addData(self, data):
        self.data = data
        
    def counts(self, count, final_count, data_columns):
        none_button = tk.Button(
            self.tkwindow, text = "None", 
            command = lambda : self.submitData(count, "None"))
        none_button.grid(row = 1, column = 2*(count) - 2)
        init_column = [x for x in data_columns]
        column_setter = self.count_menu[count - 1]
        self.row_assets.update({count : {}})
        self.value_index.update({count : {}})
        self.total.update({count : 0})
        self.label_opt_set.update({count : ['', '', '', '', '']})
        self.label_opt_set[count][0] = none_button
        self.label_opt_set[count][1] = tk.StringVar(self.tkwindow)
        self.label_opt_set[count][1].set(column_setter)
        self.label_opt_set[count][2] = tk.OptionMenu(
            self.tkwindow, self.label_opt_set[count][1], *init_column,
            command = lambda z: self.newRow(z, count))
        self.label_opt_set[count][2].grid(
            row = 2, column = 2*(count) - 2)
        self.label_opt_set[count][3] = tk.Button(
            self.tkwindow, text = "Submit Columns", 
            command = lambda: self.submitData(count, column_setter))
        self.label_opt_set[count][3].grid(
            row = 3, column = 2*(count) - 2)
        self.columns = init_column
        if final_count == 1:
            return
        self.counts(count + 1, final_count - 1, init_column)
    
    def submitData(self, count, result):
        self.label_opt_set[count][4] = result
        if len(self.value_index[count]) == 0 and result != 'None':
            return
        self.label_opt_set[count][0].destroy()
        self.label_opt_set[count][2].destroy()
        self.label_opt_set[count][3].destroy()
        self.true_data.update({count : []})
        for submittable in self.value_index[count]:
            self.row_assets[count][submittable][1].destroy()
            self.true_data[count].append(
                self.data[submittable])
        if self.label_opt_set[count][4] in self.submit_check:
            return
        if self.label_opt_set[count][4] == 'Row Names':
            self.submit_check.append('row_names')
            self.all_values.update({'row_names' : self.current_values})
            self.asker.row_names = self.current_values
            print(self.values)
        if self.label_opt_set[count][4] == 'Columns':
            self.submit_check.append('columns')
        if self.label_opt_set[count][4] == 'None':
            self.submit_check.append('None')
        if len(self.submit_check) == self.final_count:
            for the_count in self.row_assets:
                for the_value in self.row_assets[the_count]:
                    try:
                        self.data_edit[self.submit_check[the_count - 1]].append(self.data[the_value])
                    except:
                        self.data_edit.update({self.submit_check[the_count - 1] : [self.data[the_value]]})
            self.tkwindow.destroy()
            fig_prof = figureProfile(
                self.asker.current_column[self.all_values['row_names'][0]], self.asker.row_names[0])
            mainloop(fig_prof, self.asker)
    
    def newRow(self, value, count, shift = 4):
        self.columns.remove(value)
        self.current_values.append(value)
        self.replace_column(self.count, self.final_count, self.columns)
        self.row_assets[count].update({value : ['', '']})
        self.row_assets[count][value][0] = tk.Label(
            self.tkwindow, text = str(value))
        self.row_assets[count][value][1] = tk.Button(
            self.tkwindow, text = "Delete", command = lambda:
                self.deleteRow(value, count))
        self.row_assets[count][value][0].grid(
            row = self.total[count] + shift, column = 2*count - 2)
        self.row_assets[count][value][1].grid(
            row = self.total[count] + shift, column = 2*count - 1)
        self.value_index[count].update({value : self.total[count]})
        self.total[count] += 1
        
    def deleteRow(self, value, count):
        self.columns.append(value)
        self.current_values.remove(value)
        self.replace_column(self.count, self.final_count, self.columns)
        self.total[count] -= 1
        self.row_assets[count][value][0].destroy()
        self.row_assets[count][value][1].destroy()
        value_check = self.value_index[count][value]
        self.row_assets[count].pop(value)
        self.value_index[count].pop(value)
        for entry in self.value_index[count]:
            if self.value_index[count][entry] > value_check:
                new_row = self.row_assets[
                    count][entry][0].grid_info()["row"] - 1
                self.row_assets[count][entry][0].grid_forget()
                self.row_assets[count][entry][1].grid_forget()
                self.row_assets[count][entry][0].grid(
                    row = new_row, column = 2*count - 2)
                self.row_assets[count][entry][1].grid(
                    row = new_row, column = 2*count - 1)
                self.value_index[count][entry] -= 1
        
    def replace_column(self, count, final_count, new_column):
        if len(self.label_opt_set[count]) != 5:
            self.label_opt_set[count][2].grid_forget()
            self.label_opt_set[count][2] = tk.OptionMenu(
                self.tkwindow, self.label_opt_set[count][1], *new_column,
                command = lambda z: self.newRow(z, count))
            self.label_opt_set[count][2].grid(row = 2, column = 
                                              2*(count) - 2)
        if final_count == 1:
            return
        self.replace_column(count + 1, final_count - 1, new_column)
        


init_frame = tk.Tk()
init_frame.geometry("500x500")
init_frame.title("Backend Designer Start Menu")

# The label of the Tkinter submission page that indicates
# Where to submit the dataset directory
directory_text = tk.Label(init_frame,
                  text = "Enter the directory to your dataset")


# The grid addition of the previously noted label 
directory_text.grid()

# Error message contingent on given errors
error_msg = tk.Text(init_frame, height = 1, width = 20)

# The button to upload the dataset
upload_button = tk.Button(init_frame,
                        text = "Upload the dataset")

upload_button.grid()

reader = inputter.adv_inputters()
row_set = MultiData(init_frame, reader)

# The textbox of the Tkinter submission page to submit
# The dataset directory on
data_input = tk.Text(init_frame,
                   height = 5,
                   width = 20)
data_explorer = tk.Button(init_frame, text = "File Select",
                          command = lambda : data_upload(fmt = "file_exp"))
opt_check1 = tk.Label(init_frame, text = '--\n||\n--')
opt_check2 = tk.Label(init_frame, text = '--\n||\n--')
opt_msg = tk.Label(init_frame, text = 'Or select a file through File Explorer\n with the \"Select File\" button')
opt_check1.grid(row = 2, column = 2)
opt_msg.grid(row = 2, column = 3)
opt_check2.grid(row = 2, column = 4)

# The grid addition of the previously noted textbox
data_input.grid()
data_explorer.grid(row = 4, column = 3)

# List of current assets
input_assets = [directory_text, data_input, upload_button, data_explorer,
                opt_check1, opt_check2, opt_msg]

"""
Function to upload the data on the GUI
using a directory (currently limited
to CSV)
"""
def data_upload(fmt = "window"):
    try:
        error_msg.delete('1.0', 'end')
        error_msg.grid_forget()
    except:
        pass
    if fmt == "window":
        the_directory = data_input.get(1.0, "end-1c")
    if fmt == "file_exp":
        the_directory = inputter.file_browse()
    try:
        #data_set = pnd.read_csv(the_directory)
        reader.basic_read(init_input = the_directory,
                          no_inputter = True, gui = True)
        row_set.addData(reader.data)
        print(row_set.data)
        row_set.counts(1, 2, reader.checker2.values())
    except:
        error_msg.grid(row = 5)
        error_msg.insert('1.0', 'File not read')
        return
    inputter.list_destroyer(input_assets)

upload_button.bind("<Button-1>", lambda x : data_upload())

init_frame.mainloop()


