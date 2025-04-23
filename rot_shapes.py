
import turtle


# Predefined colors in hex
colors = {
    'red': '#FF0000',
    'blue': '#0000FF',
    'green': '#008000',
    'yellow': '#FFFF00',
    'black': '#000000',
    'white': '#FFFFFF',
    'orange': '#FFA500',
    'purple': '#800080'
}


def interpolate_color(start_color, end_color, factor):
    """
    Interpolate between two colors.
    factor should be between 0 and 1.
    """
    import colorsys
    
    # Convert start and end colors to RGB
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    # Convert RGB to HSV for smoother color interpolation
    def rgb_to_hsv(rgb):
        return colorsys.rgb_to_hsv(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
    
    def hsv_to_rgb(hsv):
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
        return tuple(int(x * 255) for x in rgb)
    
    # Convert hex to RGB
    start_rgb = hex_to_rgb(colors[start_color])
    end_rgb = hex_to_rgb(colors[end_color])
    
    # Convert RGB to HSV
    start_hsv = rgb_to_hsv(start_rgb)
    end_hsv = rgb_to_hsv(end_rgb)
    
    # Interpolate in HSV space
    interpolated_hsv = (
        start_hsv[0] + factor * (end_hsv[0] - start_hsv[0]),
        start_hsv[1] + factor * (end_hsv[1] - start_hsv[1]),
        start_hsv[2] + factor * (end_hsv[2] - start_hsv[2])
    )
    
    # Convert back to RGB
    interpolated_rgb = hsv_to_rgb(interpolated_hsv)
    
    # Convert to hex color string
    return '#{:02x}{:02x}{:02x}'.format(*interpolated_rgb)

def rot_shape(times:int=1, sides:int=4, side_lenght:int=150, start_color:str='red', end_color:str='purple'):
    inc_base = (360/times)
    shape_angle = 360/sides
    for i in range(times):
        # Calculate color interpolation factor
        color_factor = i / (times - 1)  # Ensures first is red, last is violet
        
        # Get interpolated color
        color = interpolate_color(start_color, end_color, color_factor)
        
        print(f"i: {i}, Color: {color}")
        
        # Set turtle color
        tt.color(color)
        
        inc_angle = 1*inc_base
        tt.left(inc_angle)
        for j in range(sides):
            tt.forward(side_lenght)
            tt.right(shape_angle)


color_list = ','.join([color for color in colors.keys()])

times = int(input("How many times? ") or 7)
sides = int(input("How many sides? ") or 7)
lenght = int(input("How long each side? ") or 100)
start_color = input("Start color: "+color_list+' ') or 'red'
while start_color not in color_list:
    start_color = input("Start color: "+color_list+' ')

end_color = input("End color: "+color_list.replace(start_color, '')+' ') or 'purple'
while end_color not in color_list:
    end_color = input("End color: "+color_list.replace(start_color, '')+' ')

tt = turtle.Turtle()
turtle.bgcolor('black')

tt.shape('turtle')

tt.color('green')

tt.speed('fastest')

rot_shape(times, sides, lenght, start_color, end_color)

turtle.done()
