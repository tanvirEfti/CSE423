##Task-01
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


bg_r, bg_g, bg_b = 0.0, 0.0, 0.0
drops = 110
raindrops = [{"x": random.uniform(0, 1000), "y": random.uniform(0, 650)} for i in range(drops)]
rain_speed = 5
wind_shift = 0 



def iterate():
    glViewport(0, 0, 1000, 650)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 650, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(bg_r, bg_g, bg_b, 1.0)
    
    

def KeyboardListener(key, x, y):
    global bg_r, bg_g, bg_b
    if key == b'n':  
        if bg_r >= 0.0:
            bg_r -= 0.05  
            bg_g -= 0.05
            bg_b -= 0.05
            print("Night")
        else:
            print("Already Night !")
            
    if key == b'm':  
        if bg_r < 1.0:
            bg_r += 0.05  
            bg_g += 0.05
            bg_b += 0.05
            print("Morning")
        else:
            print("Already Morning !")
    glutPostRedisplay() 
  
    
def specialKeyListener(key, x, y):
    global wind_shift

    if key == GLUT_KEY_LEFT:
        wind_shift += 2  

    if key == GLUT_KEY_RIGHT:
        wind_shift -= 2 

    glutPostRedisplay() 



def drawRain():
    global raindrops, wind_shift

    glColor3f(0.0, 0.0, 0.0)  
    glLineWidth(2)  
    glBegin(GL_LINES)

    for i in raindrops:
        i["y"] -= rain_speed  
        i["x"] += wind_shift  
        
    
        if i["y"] < 0:
            i["y"] = random.uniform(0, 650)
            i["x"] = random.uniform(0, 1000)  
        
            
        glVertex2f(i["x"], i["y"])
        glVertex2f(i["x"], i["y"] -12)  

    glEnd()
    glutPostRedisplay()



def drawing():
    #ground
    glColor3f(0.6, 0.3, 0.0)
    glBegin(GL_TRIANGLES)
    
    glVertex2f(0,0)
    glVertex2f(1000,0)
    glVertex2f(0,500)
    
    glVertex2f(0,500)
    glVertex2f(1000,500)
    glVertex2f(1000,0)
    
    glEnd()
    
    #bush-line
    glColor3f(0, 1, 0)
    glLineWidth(3)
    glBegin(GL_LINES)
    
    glVertex2f(0,350)
    glVertex2f(1000,350)
    glEnd()
    
    #bush-Trinagle
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 350)  
    glVertex2f(25, 465)  
    glVertex2f(50, 350)  

    glVertex2f(50, 350)  
    glVertex2f(75, 465)  
    glVertex2f(100, 350)  

    glVertex2f(100, 350)  
    glVertex2f(125, 465)  
    glVertex2f(150, 350)  

    glVertex2f(150, 350)  
    glVertex2f(175, 465)  
    glVertex2f(200, 350)  

    glVertex2f(200, 350)  
    glVertex2f(225, 465)  
    glVertex2f(250, 350)  

    glVertex2f(250, 350)  
    glVertex2f(275, 465)  
    glVertex2f(300, 350)  

    glVertex2f(300, 350)  
    glVertex2f(325, 465)  
    glVertex2f(350, 350)  

    glVertex2f(350, 350)  
    glVertex2f(375, 465)  
    glVertex2f(400, 350)  

    glVertex2f(400, 350)  
    glVertex2f(425, 465)  
    glVertex2f(450, 350)  

    glVertex2f(450, 350)  
    glVertex2f(475, 465)  
    glVertex2f(500, 350)  

    glVertex2f(500, 350)  
    glVertex2f(525, 465)  
    glVertex2f(550, 350)  

    glVertex2f(550, 350)  
    glVertex2f(575, 465)  
    glVertex2f(600, 350)  

    glVertex2f(600, 350)  
    glVertex2f(625, 465)  
    glVertex2f(650, 350)  

    glVertex2f(650, 350)  
    glVertex2f(675, 465)  
    glVertex2f(700, 350)  

    glVertex2f(700, 350)  
    glVertex2f(725, 465)  
    glVertex2f(750, 350)  

    glVertex2f(750, 350)  
    glVertex2f(775, 465)  
    glVertex2f(800, 350)  
    
    
    glVertex2f(800, 350)  
    glVertex2f(825, 465)  
    glVertex2f(850, 350)  

    glVertex2f(850, 350)  
    glVertex2f(875, 465)  
    glVertex2f(900, 350)  

    glVertex2f(900, 350)  
    glVertex2f(925, 465)  
    glVertex2f(950, 350)  

    glVertex2f(950, 350)  
    glVertex2f(975, 465)  
    glVertex2f(1000, 350)  

    glVertex2f(1000, 350)  
    glVertex2f(1025, 465)  
    glVertex2f(1050, 350)  

    glEnd()
   
    
    #House
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(225, 250)  
    glVertex2f(225, 450)  
    glVertex2f(775, 250)  
    
    
    glVertex2f(225, 450)
    glVertex2f(775, 450)
    glVertex2f(775, 250)
    glEnd()
    
    #roof
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(190, 450)
    glVertex2f(500, 550)
    glVertex2f(810, 450)
    
    glEnd()
    
    #door
    glColor3f(0.0, 0.75, 1.0)
    
    glBegin(GL_TRIANGLES)
    glVertex2f(460, 250)
    glVertex2f(460, 375)
    glVertex2f(540, 250)
    
    glVertex2f(460, 375)
    glVertex2f(540, 375)
    glVertex2f(540, 250)
    
    glEnd()
    
    #door-handle
    glPointSize(7.5)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(523, 315)
    glEnd()

    #window 
    #Left
    glColor3f(0.0, 0.75, 1.0)
    glBegin(GL_TRIANGLES)
    
    glVertex2f(345, 325)
    glVertex2f(345, 375)
    glVertex2f(430, 325)
    
    glVertex2f(345, 375)
    glVertex2f(430, 375)
    glVertex2f(430, 325)
    
    glEnd()
    
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(387.5, 325)
    glVertex2f(387.5, 375)
    
    glVertex2f(345,350)
    glVertex2f(430,350)
    glEnd()
    
    
    #right
    glColor3f(0.0, 0.75, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(575, 325)
    glVertex2f(575, 375)
    glVertex2f(660, 325)
    
    glVertex2f(575, 375)
    glVertex2f(660, 375)
    glVertex2f(660, 325)
    glEnd()
    
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(617.5, 325)
    glVertex2f(617.5, 375)
    
    glVertex2f(575,350)
    glVertex2f(660,350)
    glEnd()
    
def animate() :
    drawRain()
    glutPostRedisplay()
    
      
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate() 
    drawing()
    drawRain()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000,650) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab-01") 
glutDisplayFunc(showScreen)
glutKeyboardFunc(KeyboardListener)
glutSpecialFunc(specialKeyListener)
glutIdleFunc(animate)
glutMainLoop()

###########################################################################################################################################

