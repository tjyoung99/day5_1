def setup():
    size(400,400)
    background(255,255,255)
    frame(100,50,90,90)
    setcolor("red")
    ellipse(200,200,50,50)
    setcolor("blue")
    ellipse(300,300,50,50)
def frame(xcoordinate,ycoordinate, framewidth, frameheight):
    fill(0,0,188)
    rect(xcoordinate,ycoordinate, framewidth, frameheight)
    fill(255,255,255)
    rect(xcoordinate+20,ycoordinate+20,framewidth/2,frameheight/2)
def setcolor(colorname):
    if colorname=="red":
        fill(255,0,0)
    elif colorname=="blue":
        fill(0,0,255)
