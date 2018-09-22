"""
grid_model.py
You can clone this file and its companion grid_run.py
to easily get started on a new grid model.
It also is a handy tool to have around for testing
new features added to the base system.
"""
import random
import indra.markov as markov
import indra.markov_agent as ma
import indra.markov_env as menv
import numpy as np
import operator as op
import math

X = 0
Y = 1

# agent condition strings
NORTH = "North"
SOUTH = "South"
EAST = "East"
WEST = "West"

ALIVE = "Alive"
INFECTED = "Infected"
ZOMBIFIED = "Zombified"

NSTATES = 4
NCOND = 3

N = 0
S = 1
E = 2
W = 3

A = 0
I = 1
Z = 2

infectionCount = 0

STATE_MAP = { N: NORTH, S: SOUTH, E: EAST, W: WEST }
CONDITION_MAP = {A: ALIVE, I: INFECTED, Z: ZOMBIFIED}

class Beings(ma.MarkovAgent):
	def __init__(self, name, state, condition, infectionTime, speed):
		super().__init__(name, state, NSTATES, NCOND, condition, infectionTime, speed)
		self.name = name
		self.state = state
		self.condition = condition
        #self.isCaught = False
        self.infectionTime
		self.speed = speed
        self.infectionTime = 10
	
	def infection(self):
		self.condition = I
        
    def turnZombie(self):
        if self.name != "Zombie" && self.condition = True:
            self.name = "Zombie"
            self.condition = Z
            
    def move(self, state):
        x = self.pos[X]
        y = self.pos[Y]
        if state == N && self.condition != I:
            if self.env.is_cell_empty(x, y+1):
                self.env.move(self, x,y+1)
        elif state == S && self.condition != I:
            if self.env.is_cell_empty(x, y-1):
                self.env.move(self, x,y-1)
        elif state == E && self.condition != I:
            if self.env.is_cell_empty(x-1, y):
                self.env.move(self, x-1,y)
        elif state == W && self.condition != I:
            if self.env.is_cell_empty(x+1, y):
                self.env.move(self, x+1,y)
                
    def act(self):
        for i in range(self.speed):
            super().act()
            self.state = self.next.state
            self.move(self.state)
                
    def postact(self):
        if self.condition = I:
            infectionCount = infectionCount + 1
            
        if infectionCount == self.infectionTime:
            turnZombie()
	
class Human(Beings):

class Zombie(Beings):

"""
class TestGridAgent(ga.GridAgent):
    

    def preact(self):
        (x, y) = self.pos
		
		#logging luggage
        logging.info("With " + self.name + " we are looking around " + " x = " + str(x) + " y = " + str(y))
        logging.info(self.name + " has neighbors: ")
        for neighbor in self.neighbor_iter():
            (x1, y1) = neighbor.pos
            logging.info("    %i, %i" % (x1, y1))
		#/logging
    def postact(self):
        logging.info("Agent %s postacting" % (self.name))

class Agent(ga.GridAgent):
	def __init__():
		self.pos=(0,0);
		
"""