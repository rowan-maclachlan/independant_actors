from Actor import Actor
from Position import Position
import my_stats as st 
import params as pa

import time as t
import random as r

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

        self._map = []
            for i in range(height):
                self._map.append([ None ] * width)

    def get_all_living_actors(self):
        """
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
        for column in self.map:
            for c in column:
                if c is not None:
                    method(c)

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
                    out += c.draw() + " "
            out += "|\n"
        out += "*"
        for x in range(self.width):
            out += "-----"
        out += "*\n"
        out += " | population: "    + str(self.population) \
                + " | born: "       + str(self.total_alive) \
                + " | died: "       + str(self.total_dead)

        return out

if __name__ == "__main__":
    import sys
    import json
    from os import path
    from time import strftime

    if len(sys.argv) == 2:
        file_start = path.splitext(path.basename(sys.argv[1]))[0]
        p.init(sys.argv[1])
    else:
        file_start = 'default'
        p.init(None)

    surface_w = p.params['surface']['width']
    surface_h = p.params['surface']['height']
    gens = p.params['generations']

    surface = Surface(surface_w, surface_h)

    for i in range(surface_w * surface_h):
        c_init = Cell(surface.ID, Position(i // surface_w, i % surface_h))
        surface.ID += 1
        surface.population += 1
        surface.set(c_init.get_position(), c_init)
    
    sim_stats = list()
    
    # add initial state
    stat = s.get_stats(surface)
    sim_stats.append(stat)

    with open("data.json", "w+") as out:
        json.dump(sim_stats, out, indent=4)

    s.output_plot("plot.html", sim_stats)

