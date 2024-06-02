# Function to generate the pyramid for a given height and character
def generate_pyramid(height, char):
    for i in range(1, height + 1):
        # Calculate the number of spaces before the character on each line
        spaces = ' ' * (height - i)
        # Calculate the number of characters on each line
        chars = char * (2 * i - 1)
        # print the line of the pyramid
        print(spaces + chars)
        
#example
generate_pyramid(20, "#")
