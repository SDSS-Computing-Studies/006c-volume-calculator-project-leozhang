#!python3
# Volume Calculator
# Feel free to rename your variables

import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Leo Zhang
    # Modified: Leo Zhang
    print("Volume Calculator")
    print("author: Leo Zhang")
    print("modified by Leo Zhang")
    print("\n")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Leo zhang
    # Modified: Leo Zhang
    print("start")

    print("\n")
    print("instructions: ")
    print("this program will ask you to enter a shape that you want to calculate its volume")
    print("then you need to enter the measurements that you will use")
    print("the volume should be the answer")
    print("\n")
    print("enter yes to redo the program")
    print("enter no to end the program")
    print("\n")
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

    prompts=["Enter the radius: ","Enter the height:","Enter the width: ","enter the length: ","Enter the height of a base of a surface of a triangle: ","Enter the length of one side of a surface of a triangle: ","not availble"]
    r,h,w,l,baseheight,baselength,no=prompts
    if shape=="sphere":
        question=[r]
        return question
    elif shape=="cylinder":
        question=[r,h]
        return question
    elif shape=="cone":
        question=[r,h]
        return question
    elif shape=="cube":
        question=[w]
        return question
    elif shape=="rectangle":
        question=[h,w,l]
        return question
    elif shape=="pyramid":
        question=[h,w,l]
        return question
    elif shape=="triangular prism":
        question=[baseheight,baselength,h]
        return question
    else:
        question=[no]
        return question

        

def getInputs(question,shape):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape

    a=0
    List=[]
    for i in question:
        if shape == "sphere" or "cylinder" or "cone" or "cube" or "rectangle" or "pyramid"or "triangular prism":
            c=input(question[a])
            c=float(c)
            List.append(c)
            a+=1
        else:
            c=0
            List.append(c)
    return List
    

def Calculate(measurements,shape):

    if shape=="sphere":
        v=(4*math.pi*(measurements[0]**3))/3
        return v
    elif shape=="cylinder":
        v=math.pi*(measurements[0]**2)*measurements[1]
        return v
    elif shape=="cone":
        v=(math.pi*(measurements[0]**2)*measurements[1])/3
        return v
    elif shape=="cube":
        v=measurements[0]**3
        return v
    elif shape=="rectangle":
        v=measurements[0]*measurements[1]*measurements[2]
        return v
    elif shape=="pyramid":
        v=(measurements[0]*measurements[1]*measurements[2])/3
        return v
    elif shape=="triangular prism"   :
        v=0.5*measurements[0]*measurements[1]*measurements[2]
        return v
    else:
        v="not availble"
        return v

title()
instructions()

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit

    shape=getShape()
     # get list of questions
    questions=getParams(shape)
    # gets list of measurements
    measurements=getInputs(questions,shape)
    print("volume is "+str(Calculate(measurements,shape))) # calculate the volume

main()
while True:
    print("\n")
    a=input("continue? yes or no: ")
    print("\n")
    if a == "yes":
        main()
    else:
        print("end")
        break

