# Initial phases of a possible algorithm visualizer

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np

ARRAY = []
CURRENT = []
array = np.random.randint(low=0, high=90,size=100)
xs = np.arange(start=0,stop=1000,step=10)

def bubbleSort( array: list, asc: bool):
    global ARRAY
    i = 0
    j = 0
    if asc:
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    ARRAY.append(array.copy())
    else:
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    ARRAY.append(array.copy())

def mergeSort(arr, asc):
    global ARRAY
    if len(arr) > 1:
        mid = len(arr)//2
  
        L = arr[:mid]
  
        R = arr[mid:]
  
        mergeSort(L,asc)
  
        mergeSort(R,asc)
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            if asc:
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            else:
                if L[i] > R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            k += 1
            ARRAY.append(arr.copy())
  
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            ARRAY.append(arr.copy())
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            ARRAY.append(arr.copy())
    return arr

bubbleSort(array,True)
# A = mergeSort(array,True)
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(100.0,1000.0,100.0,1000.0)

def drawfunc():
    global CURRENT, xs
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(1.0,1.0,1.0) 
    glLineWidth(10)

    for j in range(len(CURRENT)):
        glBegin(GL_LINES)
        glVertex2f(xs[j],0)
        glVertex2f(xs[j],CURRENT[j]*10)
        glEnd()
    
    glFlush()
    glutSwapBuffers()

i = 0

def update(val):
    global CURRENT, ARRAY, i
    glutPostRedisplay()
    glutTimerFunc(int(12),update,0)
    CURRENT = ARRAY[i] if i < len(ARRAY) else ARRAY[len(ARRAY)-1]
    i = i + 1 if i < len(ARRAY) else i - 1

def main():    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowSize(1000,500)
    glutInitWindowPosition(50,100)
    glutCreateWindow("Algorithm Visualization")
    glutDisplayFunc(drawfunc)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawfunc)

    init()    
    glutMainLoop()
    print("\n\n Ending.")

if __name__ == "__main__":
    main()