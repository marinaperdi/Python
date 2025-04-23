# Draws several lines radiating out from the origin. 
import turtle
import random

class ShapeTurtle(turtle.Turtle):
    # Constructor - just copy and use for now
    def __init__(self):
        super().__init__()
        
    # It makes the turtle spin around and draw a spotted line changing its shape everytime it draws one spot.
    def forward(self, dist):
        self.right(360)
        super().forward(dist/2)
        self. up()
        super().forward(dist/2)
        self. down()
        self.shape(random.choice (["arrow", "classic", "turtle", "circle", "square"]))
        
    # It makes the turtle spin around and draw a line changing its size and color.
    def backward(self, dist):
        self.right(360)
        super().backward(dist)
        super().color(random.choice (["red", "blue", "green", "purple", "pink"]))
        self.pensize(random.randrange(1,10))
        
def main():
    # named constants
    screen_size = 500
    screen_startx = 60 # x coordinate of the left edge of the graphics window
    # Set up the window and its attributes
    wn = turtle.Screen()              
    wn.setup(screen_size, screen_size, screen_startx, 0)
    turtle_list = []
    num_turtles = 2
    num_shape_turtles = 3
    # Create a list of different colored turtles, each pointing in a different direction
    
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.right(random.randrange(350))
        t.shape("turtle")
        t.color(random.choice(['red','green','blue','yellow']))
        t.speed(10)
        turtle_list.append(t)
    
    # Create a list of different shape_turtles, each pointing in a different direction
    
    for _ in range(num_shape_turtles):
        t = ShapeTurtle()
        t.right(random.randrange(350))
        t.speed(7)     
        turtle_list.append(t)
    
    # Move each turtle forward or backward depending on the user's answer
    question= input("Do you want the turtle to move backward or forward? (b or f)")
    random_dist=random.randrange(10,25)
    if question=="b":
        for t in turtle_list:
            for _ in range(10):
                t.backward(random_dist)
    elif question=="f":
        for t in turtle_list:
            for _ in range(10):
                t.forward(random_dist)
    wn.exitonclick()
    
# Run the main function. This should be the last statement in the file.
main()
