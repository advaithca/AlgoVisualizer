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

def mergeSort(a):
    # start with least partition size of 2^0 = 1
    width = 1    
    n = len(a)                                          
    # subarray size grows by powers of 2 
    # since growth of loop condition is exponential, 
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l=0;
        while (l < n): 
            r = min(l+(width*2-1), n-1)         
            m = min(l+width-1,n-1)
            # final merge should consider 
            # unmerged sublist if input arr
            # size is not power of 2              
            merge(a, l, m, r)
            l += width*2
        # Increasing sub array size by powers of 2
        width *= 2
    return a
    
# Merge Function 
def merge(a, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
  
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            a[k] = L[i] 
            i += 1
        else: 
            a[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
    ARRAY.append(a.copy())

# bubbleSort(array,False)
mergeSort(array)
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