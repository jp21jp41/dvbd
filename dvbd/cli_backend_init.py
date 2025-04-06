# Backend Designer Initializer (CLI)
from dvbd_2 import *
import inputter

# Initial asker object
asker = inputter.adv_inputters()
# Asker user to select a file or type a directory
z = asker.basic_ask("Would you like to select a file or type in the directory?",
                    ["1.", "2."], choice_supplement = ["Select a file", "Type in a directory"])
# Running backend designer
x = run(asker, z)
# Backend designer mainloop
mainloop(x, asker)


