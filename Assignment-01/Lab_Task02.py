from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random



points = [((250, 250), (1, 1), (0.5, 0.5, 0.5))] #position, direction, color


speed = 0.1
blinking_mode = False  
blink = True  
frozen = False  


def draw_point(x, y):
    glPointSize(5)  
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    for i in points:
        x, y = i[0]
        a,b,c = i[2]


        if blinking_mode and blink:
            glColor3f(0, 0, 0)  
        else:
            glColor3f(a, b, c) 
            draw_point(x, y)
    glutSwapBuffers()


def update():
    if frozen:
        return

    global blink, blinking_mode

    for i in range(len(points)):
        (x, y), (dx, dy), color = points[i]

       
        x += dx * speed
        y += dy * speed

  
        if x <= 0 or x >= 500:
            dx *= -1
        if y <= 0 or y >= 500:
            dy *= -1

    
        points[i] = ((x, y), (dx, dy), color)

    glutPostRedisplay()  


def mouse_click(button, state, x, y):
    if frozen:
        return

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        new_x, new_y = convert_coordinates(x, y)
        new_dx = random.choice([-1, 1])
        new_dy = random.choice([-1, 1])
        new_color = (random.random(), random.random(), random.random())
        points.append(((new_x, new_y), (new_dx, new_dy), new_color))


def handle_special_keys(key, x, y):
    if frozen:
        return

    global speed, blinking_mode, blink

    if key == GLUT_KEY_UP:
        speed *= 1.5
    elif key == GLUT_KEY_DOWN:
        speed /= 1.5
    elif key == GLUT_KEY_LEFT:
        blinking_mode = not blinking_mode
        if blinking_mode:
            blink = True
            glutTimerFunc(1000, toggle_blink, 0)


def handle_keyboard(key,x,y):
    global frozen
    if key == b' ':
        frozen = not frozen


def toggle_blink(value):
    global blink
    if not frozen:
        blink = not blink
    if blinking_mode:
        glutTimerFunc(1000, toggle_blink, 0)


def convert_coordinates(x, y):
    return x, 500 - y




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Magic Box")
glutDisplayFunc(display)
glutIdleFunc(update)
glutMouseFunc(mouse_click)
glutSpecialFunc(handle_special_keys)
glutKeyboardFunc(handle_keyboard)

glutMainLoop()
