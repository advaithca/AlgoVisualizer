# Initial phases of a possible algorithm visualizer

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np

ARRAY = []
CURRENT = []
array = np.random.randint(low=0, high=100,size=100)
xs = np.arange(start=0,stop=1000,step=5)

def generate():
    global array, xs
    array = np.random.randint(low=0, high=100,size=200)
    xs = np.arange(start=0,stop=1000,step=5)

generate()
# Bubble Sort
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
#############
# Merge Sort
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

############

# Insertion Sort
def insertionSort(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                ARRAY.append(arr.copy())
        arr[j + 1] = key

##########

# Selection Sort
def selectionSort(A):
    for i in range(len(A)):
        
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        ARRAY.append(A.copy())
###########

# Quick Sort
def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
 
    for j in range(l , h):
        if   arr[j] <= x:
 
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSortIterative(arr,l,h):
 
    size = h - l + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
 
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        p = partition( arr, l, h )
 
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
        ARRAY.append(arr.copy())

###############

bubbleSort(array,True)
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
        glVertex2f(xs[j],CURRENT[j]*8)
        glEnd()
    
    glFlush()
    glutSwapBuffers()

i = 0
def update(val):
    global CURRENT, ARRAY, i
    glutPostRedisplay()
    glutTimerFunc(int(30),update,0)
    CURRENT = ARRAY[i] if i < len(ARRAY) else ARRAY[len(ARRAY)-1]
    i = i + 1 if i < len(ARRAY) else i - 1

def sortingMode(option):
    global i, ARRAY, array
    if option == 1:
        ARRAY = []
        generate()
        bubbleSort(array,True)
        glClear(GL_COLOR_BUFFER_BIT)
        i = 0
    if option == 2:
        ARRAY = []
        generate()
        bubbleSort(array,True)
        glClear(GL_COLOR_BUFFER_BIT)
        i = 0
    if option == 3:
        ARRAY = []
        generate()
        insertionSort(array)
        glClear(GL_COLOR_BUFFER_BIT)
        i = 0
    if option == 4:
        ARRAY = []
        generate()
        selectionSort(array)
        glClear(GL_COLOR_BUFFER_BIT)
        i = 0
    if option == 5:
        ARRAY = []
        generate()
        mergeSort(array)
        glClear(GL_COLOR_BUFFER_BIT)
        i = 0
    if option == 6:
        ARRAY = []
        generate()
        quickSortIterative(array,0,len(array)-1)
        glClear(GL_COLOR_BUFFER_BIT)
        i = 0

def main():    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowSize(1000,500)
    glutInitWindowPosition(50,100)
    glutCreateWindow("Algorithm Visualization (Default: Bubble Sort)")
    glutDisplayFunc(drawfunc)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawfunc)
    glutCreateMenu(sortingMode)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutAddMenuEntry("Go Again!",1)
    glutAddMenuEntry("Bubble Sort",2)
    glutAddMenuEntry("Insertion Sort",3)
    glutAddMenuEntry("Selection Sort",4)
    glutAddMenuEntry("Merge Sort",5)
    glutAddMenuEntry("Quick Sort",6)
    init()
    glutMainLoop()
    print("\n\n Ending.")

if __name__ == "__main__":
    main()