from pprint import pprint
from twophase import solve
import time

import pygame
from pygame.locals import *

from .cube import Cube
from .move import Move
from ..scramble.parser import scramble_to_moves, moves_to_scramble
from ..scramble.generator import gen_scramble
from ..scramble.cleaner import clean_moves
from .solver import generate_solution
from .colour import Colour
from ..p2.AIs import BFS,Better_BFS,A_Star,IDA_Star,Mini,State
from ..p2.Cubeai import Cubeai
from ..p2.Heuristic import Heuristic,myHeuristic
from ..p2.ManhattanCube import ManhattanCube


HEIGHT = 600
WIDTH = 700
CUBIE_SIZE = 45
HORIZONTAL_START = 100

class Gui:
    def __init__(self, cube: Cube,cube2: Cubeai):
        self.cube = cube
        self.cube2 = cube2
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.sta = ""


    def state(self):
        s = []
        order = ["U","R","F","D","L","B"]
        col = {(255, 255, 255):'U',(0, 255, 0):'F',(255, 165, 0):'L',(255, 255, 0):'D',(0, 0, 255):'B',(255, 0, 0):'R'}
        for i in order:
            for j in self.cube.faces[i]:
                for k in j:
                    s.append(col[k])
        return "".join(s)
            
    
    def scram_revt(self,s: str):
        scram_move = []
        dit = {"F":0,"U":1,"R":2,"D":3,"L":4,"B":5}
        for i in s.split(" "):
            if len(i) == 1:
                mov = (dit[i],1)
                scram_move.append(mov)
            else:
                mov = (dit[i[0]],int(i[1]))
                scram_move.append(mov)
        return scram_move
     
    def transl_path(path):
        strpath = []
        for i in range(len(path)):
            po = str(Cubeai.translateMove(path[i][0]))
            if po != "None":
                strpath.append(po)
        return " ".join(strpath)
        
        
    def run(self):
        self.draw_cube()
        print("Select the option you want to execute: \n 1 -> Scramble \nSolve: \n 2 -> Kociemba \n 3 -> Layering \n 4 -> BFS \n 5 -> Better BFS \n 6 -> A* \n 7 -> IDA* \n 8 -> Mini\n")
        running = True
        while running:
            for event in pygame.event.get():
                prime = pygame.key.get_pressed()[pygame.K_LSHIFT]
                if event.type == pygame.QUIT:
                    running = False                     
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)

                    if key == "1":
                        self.cube = Cube(3)
                        self.cube2 = Cubeai(3)
                        scramstr = gen_scramble()
                        self.cube.do_moves(scramstr)
                        for i in self.scram_revt(scramstr):
                            self.cube2.makeMove(i)
                        self.draw_cube()
                        self.sta = self.state()
                        print("Cube Scrambled!\n")
                    elif self.sta != "":
                        if key == '2':
                            print("Solving by Kociemba!")
                            solution = solve(self.sta)
                            print("Kociemba Solution Found: ",solution)
                            for move in solution.split():
                                self.cube.do_moves(move)
                                self.draw_cube()
                                time.sleep(0.1)
                            self.sta = ""
                            print('\n')
                        elif key == '3':
                            print("Solving by layering!")
                            solution = moves_to_scramble(generate_solution(self.cube))
                            print("Layering Solution Found: ",solution)
                            for move in solution.split():
                                self.cube.do_moves(move)
                                self.draw_cube()
                                time.sleep(0.1)
                            self.sta = ""
                            print('\n')
                        elif key == '4':
                            ai = BFS(self.cube2)
                            print("Solving by BFS!")
                            path = ai.solve()
                            print("BFS Solution found: ",self.transl_path(path))
                            print('\n')
                        elif key == '5':
                            ai = Better_BFS(self.cube2)
                            print("Solving by Better BFS!")
                            path = ai.solve()
                            print("Better BFS Solution found: ",self.transl_path(path))
                            print('\n')
                        elif key == '6':
                            heuristic = Heuristic.manhattanDistance
                            ai = A_Star(self.cube2,heuristic)
                            print("Solving by A*!")
                            path = ai.solve()
                            print("A* Solution found: ",self.transl_path(path))  
                            print('\n')                         
                        elif key == '7':
                            heuristic = Heuristic.manhattanDistance
                            print("Solving by IDA*!")
                            ai = IDA_Star(self.cube2,heuristic)
                            path = ai.solve()
                            print("IDA* Solution found: ",self.transl_path(path))  
                            print('\n') 
                        elif key == '8':
                            heuristic = Heuristic.manhattanDistance
                            ai = Mini(self.cube2,heuristic)
                            print("Solving by Mini!")
                            path = ai.solve()
                            print("Mini Solution found: ",self.transl_path(path))  
                            print('\n')   
                    else:
                        print("Scramble the cube first to solve it ! \n")
            
    def draw_cube(self):
        for face_num, face in enumerate(["U", "F", "D", "B", "L", "R"]):
            for row_num, row in enumerate(self.cube.faces[face]):
                for cubie_num, cubie in enumerate(row):
                    if face == "L":
                        face_num = 1
                        horizontal_adjust = - self.cube.size * CUBIE_SIZE
                    elif face == "R":
                        face_num = 1
                        horizontal_adjust = self.cube.size * CUBIE_SIZE
                    elif face == "B":
                        face_num = 1
                        horizontal_adjust = 2 * self.cube.size * CUBIE_SIZE
                    else:
                        horizontal_adjust = 0
                        
                    x = WIDTH / 3 + cubie_num * CUBIE_SIZE + horizontal_adjust
                    y = self.cube.size * face_num * CUBIE_SIZE + row_num * CUBIE_SIZE + HORIZONTAL_START
                    
                    pygame.draw.rect(self.screen, cubie, (x, y, CUBIE_SIZE, CUBIE_SIZE), 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), (x, y, CUBIE_SIZE, CUBIE_SIZE), 5)

        pygame.display.update()
