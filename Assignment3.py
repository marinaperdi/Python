""" Draw a marquee on the turtle screen. There are two turtles, one to draw a box and
    another to write, pause, and erase the text. 
    Marina Perdiguero, April, 5 2023
    """

import turtle
import time



def drawRect(t, len, wid):
    """ Draws a rectangle using turtle t with sides len and wid """
    for side in [len, wid, len, wid]:
        t.forward(side)
        t.left(90)
        
def moveTurtle(t, posx, posy):
    """ Moves the turtle where the text starts"""
    t.pu()
    t.goto(posx,posy)
    t.pd()
         
def main():
    # Values to control the display
    scroll_text = 'Marina '
    sz = len(scroll_text)
    xpos = -170
    ypos = 0
    char_width = 12
    box_height = 40
    text_offset = 10
    # End section of display adjustments
    
    # Draw the marquee box
    wn = turtle.Screen()
    boxturtle = turtle.Turtle()
    boxturtle.speed(0)
    moveTurtle(boxturtle, xpos, ypos)
    drawRect(boxturtle, sz*char_width,box_height)
    
    # Put writing turtle in marquee box
    john = turtle.Turtle()
    moveTurtle(john, xpos, ypos+text_offset)

    # For every possible marquee pattern, draw the text, wait one second, then erase
    position1=0
    position2=1
    for i in range(4 * sz):
    # If you run out of letters, go back to the begining
        if position1 == len(scroll_text)+sz:
            position1=0 
            position2=1
    # Add the amount of spaces necessary before the string
        space= " "*sz
        word=space+scroll_text
        first= word[position1]
        rest=word[position2:]
        txt=first+rest
        text=txt[1:sz]
        john.clear()
        john.write(text, font=("Courier", 16, "normal"), align="left")
        time.sleep(0.5)
        position1+=1
        position2+=1
    john.clear()
    wn.exitonclick()

main()