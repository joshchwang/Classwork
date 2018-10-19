
x = 0
y = 0
z = 0
def setup():
    size(500, 500)

def draw():
    global x
    global y
    global z
    x += 1
    y += 5
    z += 10
    if x > 625:
        x = 1
    elif y > 625:
        y = 1
    elif z > 625:
        z = 1
    else:
        background('#87CEEB')
        fill('#FFFF4D')
        ellipse(x, 50, 100, 100)
    noStroke()
    fill(255, 255, 255)
    ellipse(y, 100, 50, 50)
    ellipse(y, 125, 50, 50)
    ellipse(y + 25, 100, 50, 50)
    ellipse(y + 25, 125, 50, 50)
    ellipse(y - 25, 125, 50, 50)
    ellipse(y + 50, 125, 50, 50)
    
    fill(255, 255, 255)
    ellipse(z, 175, 50, 50)
    ellipse(z, 200, 50, 50)
    ellipse(z + 25, 175, 50, 50)
    ellipse(z + 25, 200, 50, 50)
    ellipse(z - 25, 200, 50, 50)
    ellipse(z + 50, 200, 50, 50)
