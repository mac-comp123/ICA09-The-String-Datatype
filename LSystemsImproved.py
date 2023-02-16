import turtle
import time

# --------------------------------------------------------------------------
# The main functions demonstrate how to use this code for three different fractals


def main():
    # first defines a few L-systems for fractals
    kochAxiom = "F"
    kochRules = [['F', 'F+F--F+F']]
    kochAngle = 60

    hilbertAxiom = "L"
    hilbertRules = [['L', '+RF-LFL-FR+'], ['R', '-LF+RFR+FL-']]
    hilbertAngle = 90

    islandLakeAxiom = "F+F+F+F"
    islandLakeRules = [['F', 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF'], ['f', 'ffffff']]
    islandLakeAngle = 90

    win = turtle.Screen()
    fracTurtle = turtle.Turtle()
    fracTurtle.speed(0)


    moveTurtle(fracTurtle, -200, -50)
    generateFractal(fracTurtle, 3, kochAxiom, kochRules, kochAngle, 10)

 
    win.exitonclick()


def moveTurtle(t, x, y):
    """Given a turtle object, and x and y coordinates, moves the turtle to that location
    without leaving a line behind."""
    t.up()
    t.goto(x, y)
    t.down()



def generateFractal(fTurt, recReps, axiom, rules, angle, dist=10):
    """Given a turtle, the number of recursive repetitions to do, and a specification
    of an L-system: axiom, rules, and angle, it generates the string that directs the turtle
    to move, and then draws the fractal."""

    # Build instructions with L-system
    instructions = createLSystem(recReps, axiom, rules)
    # print(instructs)

    # draw the picture
    drawLsystem(fTurt, instructions, angle, dist)



# --------------------------------------------------------------------------
# These functions take a string-based L-System and create a string by applying
# the rewriting rules


def createLSystem(numIters, axiom, rules):
    """Takes in the number of iterations of the rewriting process, the starting
    axiom, and a list of rules. Each rule is a sublist with the symbol on the lefthand side
    first, followed by a string for the righthand side. Returns the final string."""
    currString = axiom
    nextString = axiom
    for i in range(numIters):
        nextString = processString(currString, rules)
        currString = nextString
    return nextString



def processString(oldStr, rules):
    """Processes the current string by going through character by character and
    replacing each character by the application of a rule, if any. Returns the
    new string. This performs one step of the rewriting process."""
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch, rules)
    return newstr



def applyRules(ch, rules):
    """Takes in a character and the list of rules, and finds the first rule that applies
    to the character and returns the righthand side. If no rules apply the character is
    returned unchanged."""
    newstr = ""
    for rule in rules:
        lhs = rule[0]
        rhs = rule[1]
        if ch == lhs:
            return rhs
    return ch


# --------------------------------------------------------------------------
# These functions take a string giving instructions for an L-system, and a list
# that decodes the characters in the string to tell what to do with them, and
# it has a turtle trace the shape given by the instructions

def drawLsystem(aTurtle, instructions, angle, distance):
    """Takes in a turtle, a string of instructions, plus the
    angle to turn when told to turn, and the distance forward to go.
    It loops over the instructions, and does the correct action for
    each. F means go forward distance while drawing, f means go forward
    distance without drawing, + means turn left by angle, - means turn right
    by angle, and | means turn 180 degrees."""
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'f':
            aTurtle.up()
            aTurtle.forward(distance)
            aTurtle.down()
        elif cmd == '-':
            aTurtle.right(angle)
        elif cmd == '+':
            aTurtle.left(angle)
        elif cmd == '|':
            aTurtle.left(180)
        else:
            # ignore any other characters in the instructions
            pass



if __name__ == "__main__":
    main()
