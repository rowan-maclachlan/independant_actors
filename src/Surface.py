from Actor import Actor
from Position import Position
import my_stats as st 
import params as pa

import time as t
import random as r
import numpy as np

"""
These are the 9 offsets on the surface which represent
the neighbourhoord of a cell.  A cell at position (3, 5) will
have a neighbourhood of 9 positions.  From left to right and 
top to bottom, these include:
    (2, 4), (3, 4), (4, 4),
    (2, 5), (3, 5), (4, 5), and
    (2, 6), (3, 6), (4, 6)
When used to get the neighbours of any cell for its interactions,
the position which is the cell's position must be ignored.
"""
neighbour_offsets = [Position(-1,-1), Position( 0,-1), Position( 1,-1),
                     Position(-1, 0), Position( 0, 0), Position( 1, 0),
                     Position(-1, 1), Position( 0, 1), Position( 1, 1)]

class Surface:
    """
    """
    def __init__(self, width, height):
        """
        :param width: The width of the surface in open spots.
        :type width: int
        :param height: The height of the surface in open spots.
        :type height: int
        """
        self.population = 0
        self.width = width
        self.height = height
        self.total_alive = 0
        self.total_dead = 0
        self._all_cells = set()
        self.ID = 0

        self._map = []
        for i in range(height):
            self._map.append([ None ] * width)

    def tick(self):
        active_actors = self.get_active_actors()
        for actor in active_actors:
            print("actor!")

    def get_active_actors(self):
        """
        Retrieve the list of which actors will
        be active for this iteration.
        :return: A random sample of actors from all actors.
        :rtype: list(Actor)
        """
        num_active_actors = pa.params['actors_per_iter']
        all_actors = self.get_all_actors()
        active_actors = np.random.choice(all_actors, num_active_actors, replace=False)
        return active_actors

    def get_all_actors(self):
        """
        Retrieve all actors in this simulation.
        """
        living_actors = list()
        for y in range(self.height):
            for x in range(self.width):
                if self.get(Position(x, y)) is not None:
                    living_actors.append(self.get(Position(x, y)))
        return living_actors

    def get(self, pos):
        """
        """
        return self._map[(self.height + pos.y) % self.height][(self.width + pos.x) % self.width]

    def set(self, pos, c):
        """
        """
        if c is None:
            self._all_cells.remove(self.get(pos))
        else:
            self._all_cells.add(c)
        self._map[(self.height + pos.y) % self.height][(self.width + pos.x) % self.width] = c
    
    def apply_map(self, method):
        """
        Apply the method 'method' to every living Actor
        on this Surface's map.
        :param method: The function to apply to all living Actors.
        :type method: function
        """
        for column in self._map:
            for a in column:
                if a is not None:
                    method(a)

    def get_neighbours(self, actor):
        """
        """
        neighbours = set()
        for offset in neighbour_offsets:
            neighbour = self.get(actor.get_position() + offset)
            if neighbour is not None:
                neighbours.add(neighbour)
        return neighbours
    
    def get_empty_neighbour_position(self, a):
        """
        """
        candidates = []
        for offset in neighbour_offsets:
            neighbour = self.get(a.get_position() + offset)
            if neighbour is None:
                candidates.append(a.get_position() + offset)
        if len(candidates) == 0:
            return None
        return random.choice(candidates)
    
    def __str__(self):
        out = "*"
        for x in range(self.width):
            out += "-----"
        out += "*\n"
        for y in range(self.height):
            out += "|"
            for x in range(self.width):
                a = self.get(Position(x, y))
                if a is None:
                    out += "     "
                else:
                    out += a.draw() + " "
            out += "|\n"
        out += "*"
        for x in range(self.width):
            out += "-----"
        out += "*\n"
        return out

if __name__ == "__main__":
    import sys
    import json
    from os import path
    from time import strftime

    surface_w = pa.params['width']
    surface_h = pa.params['height']
    gens = pa.params['iterations']

    surface = Surface(surface_w, surface_h)

    for i in range(surface_w * surface_h):
        new_pos = Position(i // surface_w, i % surface_h)
        new_actor = Actor(surface.ID, new_pos)
        surface.ID += 1
        surface.population += 1
        surface.set(new_pos, new_actor)
    
    sim_stats = list()
    
    for i in range(pa.params['iterations']):
        surface.tick()

    
#    with open("data.json", "w+") as out:
#        json.dump(sim_stats, out, indent=4)
#
#    s.output_plot("plot.html", sim_stats)

