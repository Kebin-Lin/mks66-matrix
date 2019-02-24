#Thanks, Numberphile

from display import *
from draw import *
from matrix import *
from math import *
from copy import deepcopy

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

IDENT = new_matrix()
ident(IDENT)
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A)
print_matrix(A)
print_matrix(B)
matrix_mult(IDENT,A)
print_matrix(A)

def translate(matrix,dx,dy,dz):
    transl = new_matrix()
    ident(transl)
    lst = [dx,dy,dz]
    for i in range(3):
        transl[3][i] = lst[i]
    matrix_mult(transl,matrix)

def dilate(matrix,factor,cx = 0,cy = 0,cz = 0):
    diffCen = False
    if not(cx == 0 and cy == 0 and cz == 0):
        diffCen = True
        translate(matrix,-cx,-cy,-cz)
    for i in matrix:
        for j in range(3):
            i[j] = factor * i[j]
    if diffCen:
        translate(matrix,cx,cy,cz)

def rotate(matrix,deg,cx = 0,cy = 0,cz = 0):
    rot = new_matrix()
    ident(rot)
    rot[0][0] = cos(deg)
    rot[0][1] = sin(deg)
    rot[1][0] = -sin(deg)
    rot[1][1] = cos(deg)
    if not(cx == 0 and cy == 0 and cz == 0):
        base = new_matrix()
        ident(base)
        translate(base,-cx,-cy,-cz)
        matrix_mult(rot,base)
        translate(base,cx,cy,cz)
        rot = base
    matrix_mult(rot,matrix)

def fixMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(4):
            matrix[i][j] = int(round(matrix[i][j],0))

sides = 36
radius = 3

for i in range(sides):
    ang = pi * 2 * i / sides
    nextang = pi * 2 * (i + 1) / sides
    add_edge(matrix,radius * cos(ang), radius * sin(ang), 0, radius * cos(nextang), radius * sin(nextang), 0)

translate(matrix, 250, 250, 0)

print_matrix(matrix)
save = matrix

turns = 1000
grat = (1 + math.sqrt(5))/2

singturn = pi * grat

for i in range(turns):
    color = [int((i / turns) * 255), 255, 0]
    matrix = save
    save = deepcopy(matrix)
    transform = new_matrix()
    ident(transform)
    turnamt = i * singturn
    dist = (250 * i / turns)
    rotate(transform,turnamt,250,250,0)
    translate(matrix, dist * cos(turnamt), dist * sin(turnamt),0)
    matrix_mult(transform,matrix)
    fixMatrix(matrix)
    draw_lines(matrix, screen, color)

display(screen)
