import turtle
t = turtle
t.shape("turtle")
t.speed(3)
def star (space):
    for i in range(6):
        t.forward(space)
        t.left(144)
    t.right(space)
    t.forward(space)
    space = space + 1

star(1)