#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("Volume Calculator")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:

    return None
def getShape():
    # input: none needed
    # output: string shape
    #author
    shape=input("Enter a shape: ")
    return shape

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]

    #r=input("Enter the radius: ") # sphere, cylinder, cone
    #s=input("Enter the slant height:")
    #h=input("Enter the height:") # cube, rectangle, pyramid
    #w=input("Enter the width")
    #l=input("enter the length")
    # triangle
    #baseheight=input("Enter the height of a base of a surface of a triangle (calculate the area of the base): ")
    #baselength=input("Enter the length of one side of a surface of a triangle: ")
    if shape == "sphere":
        questions = 
    prompts=["Enter the radius: ","Enter the slant height:","Enter the height:","Enter the width","enter the length"",Enter the height of a base of a surface of a triangle (calculate the area of the base): ","Enter the length of one side of a surface of a triangle: "]

    return prompts

def getInputs(prompts):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    shape=getShape()
    r,s,h,w,l,baseheight,baselength = getParams(shape)
    if shape=="sphere":
        r=input(r)
        r=float(r)
        measurements=[r]
        return measurements
    elif shape=="cylinder":
        r=input(r)
        h=input(h)
        r=float(h)
        h=float(h)
        measurements=[r,h]
        return measurements
    elif shape=="cone":
        r=input(r)
        s=input(s)
        h=input(h)
        r,s,h=float(r,s,h)
        measurements=[r,s,h]
        return measurements
    elif shape=="cube":
        w=input(w)
        w=float(w)
        measurements=[w]
        return measurements
    elif shape=="rectangle":
        h=input(h)
        w=input(w)
        l=input(l)
        h,w,l=float(h,w,l)
        measurements=[h,w,l]
        return measurements
    elif shape=="pyramid":
        h=input(h)
        w=input(w)
        l=input(l)
        h,w,l=float(h,w,l)
        measurements=[h,w,l]
        return measurements
    elif shape=="triangle":
        baseheight=input(baseheight)
        baselength=input(baselength)
        h=input(h)
        baseheight,baselength,h=float(baseheight,baselength,h)
        measurements=[baseheight,baselength,h]
        return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    getShape() # a string
    getParams(shape) # get list of questions
    getInputs(parameters) # gets list of measurements

main()