import re

print("Our magicla calculator")
print("type quit to exit")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation =input ("enter equation:")
    else:
        equation = input(str(previous))

    if equation ==  'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()""]', '' , equation)
        if previous == 0 :
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        
        print(previous)


while run:
    performMath()
