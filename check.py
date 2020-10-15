question=['baseheight','baselength','h']
a=0
List=[]
for i in question:
    b=question[a]
    c=input(question[a])
    c=float(c)
    List.append(c)
    a+=1
print(List)

def getShape():
    # input: none needed
    # output: string shape
    #author
    shape=input("Enter a shape: ")
    return shape

    getParams(shape) # get list of questions
    getInputs(questions) # gets list of measurements