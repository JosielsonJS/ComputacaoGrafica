from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

def init():
    glClearColor(0,0,0, 1)
    glPointSize(5)

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.5,0.5)
    glVertex2f(0.0,0.75)
    glVertex2f(0.5,0.5)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.4,0.5)
    glVertex2f(-0.4,0.0)
    glVertex2f(0.4,0.0)
    glVertex2f(0.4,0.5)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.3,0.0)
    glVertex2f(-0.3,0.3)
    glVertex2f(-0.15,0.3)
    glVertex2f(-0.15,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex(0.0,0.35)
    glVertex(0.0,0.15)
    glVertex(0.3,0.15)
    glVertex(0.3,0.35)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex(0.0,0.25)
    glVertex(0.3,0.25)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex(0.15,0.35)
    glVertex(0.15,0.15)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    glutDisplayFunc(render)
    init()
    glutMainLoop()

if __name__ == "__main__":
        main()
