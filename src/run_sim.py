from Surface import Surface

import params as pa
import my_stats as st

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

