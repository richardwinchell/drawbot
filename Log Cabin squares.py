# Random Log Cabin square generator 
# by Richard Winchell (richardwinchell.com)
# ----------------------------------------

# modules

# variables
canvas = 900
rings = 5
modSize = int(canvas/((2*rings)-1))
blocks = 24

# functions
def ltColor(): # light color generator
    r=(randint(153,255)/255)
    g=(randint(153,255)/255)
    b=(randint(153,255)/255)
    return (r,g,b)

def dkColor(): # dark color generator
    r=(randint(0,102)/255)
    g=(randint(0,102)/255)
    b=(randint(0,102)/255)
    return (r,g,b)


# instructions
for b in range(blocks):
    newPage(canvas,canvas)

    # draw the center square (any color)
    translate(canvas/2,canvas/2)
    fill(random(),random(),random())
    fill(1,0,0) # always red!
    rect(-modSize/2,-modSize/2, modSize,modSize)
        
    for i in range(rings-1):
        i = i+1
        print(i)
    
        with savedState():
            # draw the right block (light color)
            if (i == 1):
                translate(modSize/2,modSize/2)
            else:
                translate((i-0.5)*modSize,(i-0.5)*modSize)
            fill(*ltColor())
            w = modSize
            h = modSize*((i)*2)
            rect(0,0, w,-h)

            # draw the bottom block (light color)
            if (i == 1):
                translate(0,-h)
            else:
                translate(0,-(i*2)*modSize)
            fill(*ltColor())
            w = modSize*(i*2)
            h = modSize
            rect(0,0, -w,h)

            # draw the left block (dark color)
            if (i == 1):
                translate(-w,h)
            else:
                translate(-(i*2)*modSize,h)
            fill(*dkColor())
            w = modSize
            h = modSize*(i*2)
            rect(0,0, w,h)

            # draw the top block (dark color)
            if (i == 1):
                translate(w,h/2)
            else:
                translate(modSize,((2*i)-1)*modSize)
            fill(*dkColor())
            w = modSize*(i*2)
            h = modSize
            rect(0,0, w,h)
        
        
saveImage('~/Desktop/log_cabins.pdf')