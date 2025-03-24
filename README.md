# dvbd
Data Visualization Backend Designer (WIP)

Backend Designer which takes a dataset directory, allows the user to select a column of data, and run plots based on the data.
So far, said plots can be saved.
Possible options:
- Histogram
- Bar Graph
- Boxplot
- Distribution
- Pie (Pre-alpha, therefore not functional)
- Table (Pre-alpha)
- Extra (Pre-alpha)
- Regression

There are many problems inherently latent within such a vast system. These issues would have to be sorted through with time, with a heavy focus on providing sound logic throughout.

Notable Issues:
1. Directory Selection: could have directory in window instead of command-line, could have the ability to access file explorer.
2. Column Selection: could have multiple based in tkinter window (as either command-line or option menu)
3. Plot Labels can be added
4. Pie Chart lacking functionality (particularly regarding color change)
5. Color selection missing in Boxplot
6. GreyScale color selection option missing
7. Cannot be automated per file/column
8. No Restart button

And much more.
The complexity of the backend designer may require switching to a compiled language (or using other means) to allow development to be performed with greater ease. At the minimum, further components may be created in a different language, as files can not only be saved, but immediately uploaded to a new or existing Word document, for example - such tasks 
could be performed in Java or another compiled language.

Basic Instructions:
1. Run dvbd_init.
2. Enter your directory into the command line.
3. Select the plot of your choice in Tkinter.
4. Make your selections and save if you would like the figure saved.

# Note that there is only one developer: changes take time.
