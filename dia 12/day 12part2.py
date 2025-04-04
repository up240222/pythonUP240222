#Exercises: Level 2
#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(number=6):
    import random
    hexa_colors=[]
    for x in range(number):  
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  
        hexa_colors.append(color) 
    return hexa_colors
print(list_of_hexa_colors())

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random
def list_of_rgb_colors(n=3):
    rgb_colors = []
    for x in range(n):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        rgb_colors.append((red, green, blue))
    return rgb_colors
print(list_of_rgb_colors(5))

#Write a function generate_colors which can generate any number of hexa or rgb colors
import random
colors=[]
def generate_colors(n=5, color_type='hex'):
    if color_type == "hex":
        for i in range(n): 
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            colors.append(color)
    
    elif color_type == "rgb":
        for i in range(n):  
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            colors.append((red, green, blue))
    
    else:

        return "Error: color_type debe ser 'hex' o 'rgb'"
    
    return colors
hex_colors = generate_colors(5, "hex")
print("Colores Hexadecimales:", hex_colors)
rgb_colors = generate_colors(5, "rgb")
print("Colores RGB:", rgb_colors)
print(generate_colors())


    

