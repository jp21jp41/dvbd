# Digit Operations (dig_ops)

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
    