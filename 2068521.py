from graphics import *

# Elliot Gardner-Medwin, number: 2068521

def draw_tri(tri_bl, tri_top, tri_br, colour, win): # basic function to draw a triangle
    tri = Polygon(tri_bl, tri_top, tri_br)
    tri.setOutline('black')
    tri.setWidth(1)
    tri.setFill(colour)
    tri.draw(win)

def draw_rec(p1, p2, colour, win): # basic function to draw a rectangle
    rec = Rectangle(p1, p2)
    rec.setFill(colour)
    rec.setOutline('black')
    rec.setWidth(1)
    rec.draw(win)

def draw_line(p1, p2, win):
    line1 = Line(p1, p2)
    line1.setFill('grey')
    line1.setWidth(1)
    line1.draw(win)

def outline(tl, br, win): # function do draw an outline for a patch
    tr = Point(br.getX(), tl.getY())
    bl = Point(tl.getX(), br.getY())
    top  = draw_line(tl, tr, win)
    right = draw_line(tr, br, win)
    bottom = draw_line(br, bl, win)
    left = draw_line(tl, bl, win)

def final_num_patch(win, tl, br, colour): 
    bl = Point(tl.getX(), br.getY()) # this gets the bottom left point
    p1 = Point(bl.getX(), bl.getY() - 10)
    p2 = Point(bl.getX() + 10, bl.getY()) # 10 is hard coded as thats the length/height of the squares in a 100x100 patch
    for i in range(10): # this draws the 10 rectangles and changes their base points every time 
        draw_rec(p1, p2, colour, win)
        p1 = Point(p1.getX() + 10, p1.getY() - 10) 
        p2 = Point(p2.getX() + 10, p2.getY() - 10)
    outline(tl, br, win)

def penultimate_line_1(win, tl, colour): # this draws the first line in the triangle patch
    tlX,tlY = tl.getX(),tl.getY()
    tri_bl,tri_top,tri_br = Point(tlX, tlY + 20),Point(tlX + 10, tlY),Point(tlX + 20, tlY + 20)
    for triangle in range(5):
        draw_tri(tri_bl, tri_top, tri_br, colour, win)
        tri_bl = Point(tri_bl.getX() + 20, tri_bl.getY())
        tri_top = Point(tri_top.getX() + 20, tri_top.getY())
        tri_br = Point(tri_br.getX() + 20, tri_br.getY())

def penultimate_line_2(win, tl, br, colour): # this draws the second line in the triangle patch
    brX = br.getX()
    tlY,tlX = tl.getY(),tl.getX()
    tri_bl,tri_top,tri_br = Point(tlX + 10, tlY + 40),Point(tlX + 20, tlY + 20),Point(tlX + 30, tlY + 40)
    for triangle in range(4):
        draw_tri(tri_bl, tri_top, tri_br, colour, win)
        tri_bl = Point(tri_bl.getX() + 20, tri_bl.getY())
        tri_top = Point(tri_top.getX() + 20, tri_top.getY())
        tri_br = Point(tri_br.getX() + 20, tri_br.getY())
    draw_tri(Point(tlX, tlY + 40), Point(tlX, tlY + 20), Point(tlX + 10, tlY + 40), colour, win) # this draws half tri 
    draw_tri(Point(brX, tlY + 40), Point(brX, tlY + 20), Point(brX - 10, tlY + 40), colour, win)

def draw_penultimate_patch(win, tl, br, colour): # this creates the triangle patch using each triangle line, changing the Y cord when needed
    penultimate_line_1(win, tl, colour)
    penultimate_line_2(win, tl, br, colour)
    penultimate_line_1(win, Point(tl.getX(), tl.getY() + 40), colour) # + 40 due to the patch sizes being 100x100, this would skip by two lines
    penultimate_line_2(win, Point(tl.getX(), tl.getY() + 40), br, colour)
    penultimate_line_1(win, Point(tl.getX(), tl.getY() + 80), colour)
    outline(tl, br, win)

def antipenultimate_patch(): # i used 3 numbers; 0, 1, 2. each to differentiate between patch/colour
    five = [
            0, 0, 0, 0, 0, # even though they dont need to be, the arrays are in the pattern, to make it easier on the eyes
            1, 0, 0, 0, 2, 
            1, 1, 0, 2, 2, 
            1, 0, 0, 0, 2, 
            0, 0, 0, 0, 0]

    seven = [
            0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 2,
            1, 1, 0, 0, 0, 2, 2,
            1, 1, 1, 0, 2, 2, 2,
            1, 1, 0, 0, 0, 2, 2,
            1, 0, 0, 0, 0, 0, 2,
            0, 0, 0, 0, 0, 0, 0]

    nine = [
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 2,
            1, 1, 0, 0, 0, 0, 0, 2, 2,
            1, 1, 1, 0, 0, 0, 2, 2, 2,
            1, 1, 1, 1, 0, 2, 2, 2, 2,
            1, 1, 1, 0, 0, 0, 2, 2, 2,
            1, 1, 0, 0, 0, 0, 0, 2, 2,
            1, 0, 0, 0, 0, 0, 0, 0, 2,
            0, 0, 0, 0, 0, 0, 0, 0, 0]

    win = GraphWin("", 100*winLength, 100*winLength) # winLength  = the user's input eg: 5, 7 or 9
    backround = draw_rec(Point(0, 0), Point(winLength*100, winLength*100), 'white', win)
    x=0
    y=0

    if winLength == 5: # this determines which array to use
        patch=five
    elif winLength==7:
        patch=seven
    else:
        patch=nine

    for number in patch: # this draws each patch for its designated number
        if number == 1:
            draw_penultimate_patch(win, Point(x, y), Point(x + 100, y + 100), colour2)
        elif number == 0:
            final_num_patch(win, Point(x, y), Point(x + 100, y + 100), colour1)
        else:
            draw_penultimate_patch(win, Point(x, y), Point(x + 100, y + 100), colour3)

        x = x + 100 # changes its X cord every time by 100

        if x==winLength*100: # this changes the Y cord whenever the X cord reach the max patch length eg 500, and rests the X cord back to 0
            x=0
            y = y + 100
        
    win.getMouse()
        
def usr_dimension(): # this validates what dimenstion the user wants
    global winLength
    print("possible dimension's; [5], [7], [9]")
    x = True
    while x:
        winLength = input("Please enter the patch dimension: ")
        if winLength == '5' or winLength == '7' or winLength == '9':
            x = False
            winLength = int(winLength)
        else:
            print("invalid input, please try again")

def usr_colour(): # this validates what colour the user wants
    colours = ['red', 'green', 'blue', 'magenta', 'cyan', 'orange'] # the colours list is in the same order as the colour initial list, so the index number in one is the same as the other
    colourinitial = ['r', 'g', 'b', 'm', 'c', 'o']

    y = True
    while y:
        colour = input("please pick the letter of the colour you want: ")
        if colour in colourinitial:
            a = colourinitial.index(colour) # finds what position the input is within the intial list
            fullcolour = colours[a] # uses the position to find the p
            y = False
            return fullcolour
        else:
            print("invalid input, please try again:")

def main(): # chooses the functions in order
    global colour1,colour2,colour3
    usr_dimension()
    print("possible colours; [r]ed, [g]reen, [b]lue, [m]agenta, [c]yan, [o]range")
    colour1 = usr_colour()
    colour2 = usr_colour()
    colour3 = usr_colour()

    antipenultimate_patch()

main()