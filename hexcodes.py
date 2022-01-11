
def to_hex(x):
    hex_base= tuple([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"])
    if((x<=255) & (x%1==0)):
        
        first = x//16
        second = x%16
        if(first>0):
            hex_answer = "{}{}" .format(hex_base[first],hex_base [second])
        else:
            hex_answer = "{}" .format(hex_base[second])
        return hex_answer
    else:
        print("Not valid number")
        return None

def hex_color(red,green,blue):
    if(len(to_hex(red))==1):
        red2 = "0"+to_hex(red)
    else:
        red2 = to_hex(red)
    if(len(to_hex(green))==1):
        green2 = "0"+to_hex(green)
    else:
        green2 = to_hex(green)
    if(len(to_hex(blue))==1):
        blue2 = "0"+to_hex(blue)
    else:
        blue2 = to_hex(blue)
    return "#"+ red2 + green2 + blue2