sun = 0
cloud1 = 0
cloud2 = 0
moon = 0
#sicloud2e of window
def setup():
  size(500,500)
#main
def draw():
    if sun >= 0:
        fill("#87CEEB")
        rect(0, 0, 500, 500)
    if moon >= 500:
        fill(0)
        rect(0, 0, 500, 500)
    global sun, cloud1, cloud2, moon
    noStroke()
    cloud1 += 1.1
    cloud2 += 1.5
    print(sun)
    if cloud1 > 625:
        cloud1 = -50
    if cloud2 > 635:
        cloud2 = -25
        
    fill('#FDB813')
    ellipse(sun, 50, 100, 100)
    if sun >= 550:
        sun = -500
    sun += 1
    fill(255)
    ellipse(moon-575, 50, 100, 100)
    fill(0)
    ellipse(moon - 550, 50, 100, 100)
    if moon >= 1000:
        moon = -50
    moon += 1
        
        
        
    #sky blue
    fill('#FFFF4D')
    #the sun
    ellipse(sun, 50, 100, 100)
    #cloud 1
    fill(255)
    ellipse(cloud1, 100, 50, 50)
    ellipse(cloud1, 125, 50, 50)
    ellipse(cloud1 + 25, 100, 50, 50)
    ellipse(cloud1 + 25, 125, 50, 50)
    ellipse(cloud1 - 25, 125, 50, 50)
    ellipse(cloud1 + 50, 125, 50, 50)
    #cloud 2 (slightly lower)
    fill(225)
    ellipse(cloud2, 175, 50, 50)
    ellipse(cloud2, 200, 50, 50)
    ellipse(cloud2 + 25, 175, 50, 50)
    ellipse(cloud2 + 25, 200, 50, 50)
    ellipse(cloud2 - 25, 200, 50, 50)
    ellipse(cloud2 + 50, 200, 50, 50)
    #mountain
    fill('#867e70')
    triangle(275, 450, 375, 200, 475, 450)
 #snow on mountain
    fill(255)
    triangle(355, 250, 375, 200, 395, 250)
    #grass
    fill('#7cfc00')
    rect(0, 400, 500, 300)
    #house
    fill('#D4B895')
    rect(200, 350, 50, 50)
    #roof of house
    fill('#9d6055')
    triangle(200, 350, 225, 300, 250, 350)
    #left window
    fill('#87CEEB')
    rect(205, 360, 15, 15)
    #right window
    fill('#87CEEB')
    rect(230, 360, 15, 15)
    #door
    fill('#9d6055')
    rect(220, 375, 10, 25)
    #doorknob
    fill(212, 175, 55)
    rect(222, 385, 3, 3)
    #THE T R EE
    fill('#6B5425')
    rect(100, 300, 30, 100)
    fill('#3A5F0B')
    ellipse(100, 300, 30, 30)
    ellipse(130, 300, 30, 30)
    ellipse(115, 300, 30, 30)     
    ellipse(95, 310, 30, 30)
    ellipse(135, 310, 30, 30)
    ellipse(135, 300, 30, 30)
    ellipse(95, 300, 30, 30)
    ellipse(100, 300, 30, 30)
    ellipse(100, 290, 30, 30)
    ellipse(130, 290, 30, 30)
    ellipse(115, 290, 30, 30)
    ellipse(115, 285, 30, 30)
         
