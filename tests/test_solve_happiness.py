# test_solve_happiness.py

import unittest
import sys
import os
lib_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "examples")
sys.path.append(lib_fldr)
import example_solve_happiness as mod_happy

all_people = []
all_people.append(mod_happy.Person('Gand', {'tax_min':0.3, 'tax_max':0.5, 'tradition':0.2, 'equity':0.9}))
all_people.append(mod_happy.Person('Murd', {'tax_min':0.0, 'tax_max':0.2,'tradition':0.5, 'equity':0.1}))

all_worlds = []
all_worlds.append(mod_happy.World('Astr', 5000, 0.1, .2, 0.3))
all_worlds.append(mod_happy.World('Cryx', 1000, 0.3, .3, 0.5))

class PlanPuzzleSlidingBlock(unittest.TestCase):
    
    def test_01_(self):
        for people in all_people:
            for world in all_worlds:
                print(mod_happy.Happiness(people, world))
                self.assertEqual(len(str(world)) > 15, True)

        
if __name__ == '__main__':
    unittest.main()