# Digit Operations (dig_ops)
from matplotlib.path import Path
import math
import numpy as np
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Polygon, Wedge

hex_strings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "A", "B", "C", "D", "E", "F"]

def hex_to_rgba(hex_value, a = 1):
    try:
        r1 = (hex_strings.index(hex_value[1]) 
              + hex_strings.index(hex_value[2]) * 16) / 256
        g1 = (hex_strings.index(hex_value[3]) 
        + hex_strings.index(hex_value[4]) * 16) / 256
        b1 = (hex_strings.index(hex_value[5]) 
        + hex_strings.index(hex_value[6]) * 16) / 256
        return((r1, g1, b1, a))
    except:
        return("g")
    
def hex_to_int(hex_value):
    value = 0
    hex_pwr = 1
    for i in range(len(hex_value)):
        value += hex_pwr * hex_strings.index(hex_value[len(hex_value) - i - 1])
        hex_pwr *= 16
    return value


def digits(integer, digit_count):
    integer = str(integer)
    while len(integer) < digit_count:
        integer = "0" + integer
    return integer

def hex(integer, total = ""):
    if integer / 16 >= 1:
        new_integer = integer // 16
        remainder = integer % 16
        hex_dig = hex_strings[remainder]
        total = hex_dig + total
        return(hex(new_integer, total))
    else:
        hex_dig = hex_strings[integer]
        return(hex_dig + total)
    


class CoordCircle:
    def __init__(self, init_coords, sum):
        self.coords = init_coords
        self.coord_codes = [Path.MOVETO]
        self.sum = sum
        self.total_rad = 0
    #
    def coord_circle(self, data, ax, color, point = 0, base_sum1 = 0):
        try:
            base_sum1 += data[point]
            base_sum2 = base_sum1 + data[point]
        except:
            return
        print(360*base_sum1/self.sum)
        #self.coords.append((self.coords[0][0] + 0.3*math.cos(2*self.total_rad), self.coords[0][1] + 0.3*math.sin(2*self.total_rad)))
        # Initial circle center
        current_coords = [self.coords[0]]
        current_codes = [Path.MOVETO]
        # First arcpoint append
        current_coords.append((self.coords[0][0] + 0.3*math.cos(self.total_rad), self.coords[0][1] + 0.3*math.sin(self.total_rad)))
        current_codes.append(Path.LINETO)
        # Total Radians addition
        self.total_rad += np.deg2rad(360*base_sum1/self.sum)
        # Point increment
        point += 1
        # Pieces in between
        self.coord_piece(data, ax, color, base_sum1, base_sum2, current_coords, current_codes, self.total_rad)
        path = Path(current_coords, current_codes)
        patch = patches.PathPatch(path, facecolor = color)
        ax.add_patch(patch)
        self.coord_circle(data, ax, color, point, base_sum1)
    
    def coord_piece(self, data, ax, color, value_1, value_2, current_coords, current_codes, radians, inftes = 1):
        if inftes == 100:
            current_coords.append(current_coords[0])
            current_codes.append(Path.CLOSEPOLY)
            #path = Path(current_coords, current_codes)
            #patch = patches.PathPatch(path, facecolor = color)
            #ax.add_patch(patch)
            return
        
        radians += np.deg2rad(360*(value_1 + (value_2 - value_1)*(inftes/100))/(self.sum*100))
        current_coords.append((current_coords[0][0] + 0.3*math.cos(radians), current_coords[0][1] + 0.3*math.sin(radians)))
        current_codes.append(Path.LINETO)
        inftes += 1
        self.coord_piece(data, ax, color, value_1, value_2, current_coords, current_codes, radians, inftes)
        
        
        
    
    """Original circle
    def coord_circle(self, data, ax, color, point):
        if point == len(data):
            self.coords.append(self.coords[0])
            self.coord_codes.append(Path.CLOSEPOLY)
            self.path = Path(self.coords, self.coord_codes)
            return
        value = data[point]
        self.total_rad += np.deg2rad(360*value/self.sum)
        self.coords.append((self.coords[0][0] + 0.3*math.cos(2*self.total_rad), self.coords[0][1] + 0.3*math.sin(2*self.total_rad)))
        self.coord_codes.append(Path.LINETO)
        point += 1
        self.coord_circle(data, point)
    """

