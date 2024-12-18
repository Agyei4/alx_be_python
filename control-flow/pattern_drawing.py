#code to draw a pattern by entering the size of the pattern

size = int(input("Enter the size of the pattern: ")) # eg. 4
completion = 1
form_of_shape = "*"

#prints the height of the square
while completion <= size:
    print(form_of_shape,end = "")
    #prints the width of the square plus 1
    for i in range(1,size + 1):
        print(form_of_shape,end = "")
    completion+=1
    print()

