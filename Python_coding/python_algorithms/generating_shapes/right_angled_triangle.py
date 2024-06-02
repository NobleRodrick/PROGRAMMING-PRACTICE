# function to generate a right angled triangle with a given height and character
def generate_triangle(height, char):
    for i in range(1, height + 1):
        # print a line of the triangle
        print(char * i)
        

#example
generate_triangle(6, " # ")