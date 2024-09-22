# Rodrigo Castellanos Rodriguez A01643147 

import turtle  # module for creating graphics and drawings 
import time     # module for working with time in Python 
import random   # module for generating random numbers 

delay = 0.1  # delay to control the game speed

# Scores 
score = 0  # variable for the score
high_score = 0  # variable for the highest score

# Screen 
window = turtle.Screen()  # variable for the game window, creates an instance of the Screen class
window.title("Snake Game")  # title of the window 
window.bgcolor("black")  # sets the background color of the window 
window.setup(width=600, height=600)  # configures the dimensions of the window
window.tracer(0)  # the window will not update automatically after drawing something

# Snake head 
head = turtle.Turtle()  # variable for the head, creates an instance of the Turtle class
head.speed(0)  # prevents the turtle from moving automatically when created
head.shape("square")  # shape of the head
head.color("purple")  # color of the head
head.penup()  # prevents the snake from leaving a trail while moving
head.goto(0, 0)  # starting position of the head
head.direction = "stop"  # sets the initial direction to stop 

# Snake food 
food = turtle.Turtle()  # variable for the food, creates an instance of the Turtle class
food.speed(0)  # prevents the food from moving automatically when created
food.shape("circle")  # shape of the food
food.color("red")  # color of the food 
food.penup()  # prevents the food from leaving a trail while moving 
food.goto(-20, 80)  # starting position of the food 

segments = []  # list of additional snake segments

# Pen 
pen = turtle.Turtle()  # variable to display text, creates an instance of the Turtle class
pen.speed(0)  # the turtle is only used for drawing text, no need to move 
pen.color("pink")  # color of the text in the window
pen.penup()  # prevents leaving a trail when moving 
pen.hideturtle()  # hides the turtle so it's not visible, only the text is visible
pen.goto(0, 260)  # position to display the score text
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 25, "normal"))  # uses the write method to display the scores

# Functions for head movement 
def go_up():  # checks if the current direction is not down, if so changes the direction to up 
    if head.direction != "down":
        head.direction = "up"

def go_down():  # checks if the current direction is not up, if so changes the direction to down
    if head.direction != "up":
        head.direction = "down"

def go_left():  # checks if the current direction is not right, if so changes the direction to left
    if head.direction != "right":
        head.direction = "left"

def go_right():  # checks if the current direction is not left, if so changes the direction to right  
    if head.direction != "left":
        head.direction = "right"

def move():  # function to adjust the head's coordinates depending on the direction
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)  # adds to the y-axis

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)  # subtracts from the y-axis

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)  # subtracts from the x-axis

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)  # adds to the x-axis

# Keyboard bindings
window.listen()  # makes the window respond to keyboard input
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main game loop
while True:  # infinite loop to run the game until manually closed 
    window.update()  # calls the update method on the graphic window to refresh the screen 

    # Check for collision of the head with the borders 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:  # defines the screen edges 
        time.sleep(1)  # pauses the game to indicate the crash 
        head.goto(0, 0)  # resets the head position
        head.direction = "stop"  # stops the head movement to rest

        # Hide the snake segments by moving them off-screen 
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the list of snake segments to reset to just the head
        segments.clear()

        # Reset score
        score = 0

        # Reset delay
        delay = 0.1

        pen.clear()  # clear the current score text 
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))  # write the updated score text

    # Check for collision with the food
    if head.distance(food) < 20:  # if the head is less than 20 pixels from the food, consider it a collision
        # Move the food to a random position within the game boundaries
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)  # move the food to the new random position

        # Add a segment to the snake
        new_segment = turtle.Turtle()  # create a new segment of the snake
        new_segment.speed(0)  # ensures the segment starts at rest
        new_segment.shape("circle")  # defines the shape of the segment
        new_segment.color("purple")  # defines the color of the segment
        new_segment.penup()  # prevents it from leaving a trail when moving
        segments.append(new_segment)  # adds the new segment to the list of segments

        # Make the delay shorter so that the snake moves faster each time it eats, making the game more challenging 
        delay -= 0.001

        # Increment score
        score += 1

        if score > high_score:  # if the current score is greater than the high score, update the high score
            high_score = score

        pen.clear()  # clear the current score text 
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))  # update the scores

    # Move the segments in reverse order 
    for index in range(len(segments) - 1, 0, -1):  # iterate through segments from last to second 
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)  # update the current segment's coordinates to follow the previous segment

    # Move segment 0 to the head's position
    if len(segments) > 0:  # moves to the snake head position to follow it
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()  # function that moves the snake head in the current direction

    # Check for collision of the head with the segments
    for segment in segments:
        if segment.distance(head) < 20:  # if the distance from the head to a segment is less than 20 pixels, consider it a collision
            time.sleep(1)  # pause the game for a second to visualize the crash 
            head.goto(0, 0)  # reset the head position 
            head.direction = "stop"  # stop the head to rest

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the list of segments
            segments.clear()

            # Reset score
            score = 0

            # Reset the delay to reset game speed
            delay = 0.1

            # Update scores 
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

    time.sleep(delay)  # the main loop waits a determined amount of time before continuing 

window.mainloop()  # starts the main game loop and keeps the game window open until manually closed
