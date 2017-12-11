from aocd import data

steps = data.split(',')

class Program(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.furthest = 0

    def move(self, direction):
        if direction == 'n':
            self.y += 1
            self.z -= 1
        elif direction == 'ne':
            self.z -= 1
            self.x += 1
        elif direction == 'nw':
            self.y += 1
            self.x -= 1
        elif direction == 's':
            self.y -= 1
            self.z += 1
        elif direction == 'se':
            self.y -= 1
            self.x += 1
        else:
            self.z += 1
            self.x -= 1

        this_dist = self.dist_from_pt()
        self.furthest = this_dist if this_dist > self.furthest else self.furthest

    def dist_from_pt(self, pt_x=0, pt_y=0, pt_z=0):
        # Calculates manhattan distance from x,y,z point
        return (abs(self.x - pt_x) + \
                abs(self.y - pt_y) + \
                abs(self.z - pt_z)) / 2

p = Program()
for s in steps:
    p.move(s)

print("P1: {}".format(p.dist_from_pt()))
print("P2: {}".format(p.furthest))
