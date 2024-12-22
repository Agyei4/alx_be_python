#code to draw a pattern by entering the size of the pattern

size = int(input("Enter the size of the pattern: ")) # eg. 4
completion = 1
form_of_shape = "*"

#prints the height of the square
while completion <= size:
    print(form_of_shape,end = "")
    #prints the width of the square plus 1
    for i in range(1,size ):
        print("*",end = "")
    completion+=1
    print()

# /tmp/correction/1065969682288550274532497439058489370187_5/100740/780490/control-flow/pattern_drawing.py doesn't contain
# print\s*\(\s*['\"]\*\s*['\"]\s*,\s*end\s*=\s*

