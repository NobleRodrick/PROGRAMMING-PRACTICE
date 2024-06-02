# Function to generate a rectangle with given width, height and character
def generate_rectangle(width, height, char):
    for i in range(height):
        # Print a line of the rectangle
        print(char * width)
        
generate_rectangle(10, 4, "*")