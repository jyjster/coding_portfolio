'''

By: Jordan Y. Jackson
Last Modified: 11/11/19, 11PM

REFERENCES

    code for coding a fractal tree graphic in Python via turtle
        https://www.simplifiedpython.net/python-turtle-module/

'''
import random

# you are the turtle
import turtle as you

shell = you.Turtle()


branch = 6 * random.randint(10, 20)

shell.penup()
shell.goto(0, -branch)
shell.pendown()

shell.left(90)

shell.speed(random.randint(5, 15))

shell.color('Black')
shell.pensize(3)
shell.screen.title("Your Tree")

# can't separate a turtle from its shell
    # similar to how you can't separate yourself/change/life/progress from chaos
turtle = ('body', 'shell')
try:
    turtle.pop()
except:
    print("can't separate")


# life is defined in terms of chaos
def life(chaos = 100):
    
    road_taken = ["Lemon Chiffon", "Dim Gray", "Slate Gray", "Cadet Blue", "Medium Aquamarine", "Dark Khaki", "Khaki", "Light Sea Green", "Dark Slate Gray", "Peach Puff", "Gold", "Light Goldenrod", "Goldenrod", "Dark Goldenrod", "Indian Red", "Saddle Brown", "Sienna", "Peru", "Burlywood", "Sandy Brown", "Chocolate", "Firebrick", "Brown", "Black"]
    shell.color(random.choice(road_taken))

    if chaos < 10:
        return "no chance for positive change"
    
    else:
        # before the fire, initializing variables
        yes, a_little, on = 30, 30, 60
        struggle, fury, flames, burning = 0, 0, 0, 0

        # fire begins
        fire = shell
        
        # growth is fire / growth is like fire
        growth = fire

        # sometimes it's needed
        sometimes_is_needed = [True, False][random.randint(0,1)]
        
        # don't fear it or run away
        ['inhibitions', 'doubt', 'fear'].clear()
        
        # go forward into the fire, into the chaos
        fire.forward(chaos)
        
        # clear out any debris
        ['regrets', 'debris'].clear()
        

        # you struggle, it burns. it will hurt and there will be pain.
                   # the longer the fire, the more pain
                   # planting the seeds for what's to come / what comes next
        for moment in range(len('chaos')):
            flames += 1
            struggle *= 2
            fury += 1
            burning *= 2
        
 
        fire.left(a_little)
        
        # the fire dies down, the chaos also
        less_chaos = 3 * chaos / 4
        
        # life returns to a period of
        life(less_chaos)
    
        # ashes are remaining
        ashes = fire
        # the ashes have new life
        grow = ashes
        
        # from the ashes/seeds you grow
        grow.right(on)
        life(less_chaos)
        
        # the fire is done for now. it has has gone/left. the fire has ran its course
        fire.left(yes)
        
        # you go back to/visit where you were before the chaos/fire
        fire.backward(chaos)
        
        return "sprout of life"

# return as a tree
tree = shell

print(life(branch))
print("tree")

# we look forward to how you grow
you.done()
print("done for now...")
