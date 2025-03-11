# dvbd
Data Visualization Backend Designer (WIP)

Backend Designer which takes a dataset directory, allows the user to select a column of data, and run plots based on the data.

Issues:
1. Directory Selection: could have directory in window instead of command-line, could have the ability to access file explorer.
2. Column Selection: could have multiple based in tkinter window (as either command-line or option menu)
3. Plot Labels can be added
4. Pie Chart lacking functionality (particularly regarding color change)
5. Color selection missing in Boxplot
6. The amount of possible selection in the Color Selection Window is only limited to 0% blue and 100% blue. The color canvases are designed using basic code automation with Java. The automation allows _most_ of the code to run, though a minute amount remains that needs to be manually added (thereby requiring the remainder of the canvas integration to be done manually).
7. GreyScale color selection option missing
8. Cannot be automated per file/column
9. No Exit/Restart button

And much more.

Basic Instructions:
1. Run dvbd_init.
2. Enter your directory into the command line.
3. Select the plot of your choice in Tkinter.
4. Make your selections and save if you would like the figure saved.

# Note that there is only one developer: changes take time.
