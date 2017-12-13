from aocd import data


class Scanner(object):
    def __init__(self, sc_range):
        self.sc_range = int(sc_range)
        sc_rng_ls = list(range(self.sc_range))
        self.positions = [i for i in sc_rng_ls + sc_rng_ls[-2:-int(sc_range): -1]]

    def pos_at_pico(self, pico):
        #Gets the position of a scanner within its range at a given pico second
        return self.positions[pico % len(self.positions)]


class Journey(object):
    def __init__(self, scanners):
        self.scanners = scanners
        self.total_depth = max([int(k) for k in scanners.keys()])

    def severity(self, delay=0):
        severity_counter = 0
        collision = False
        for depth in range(self.total_depth):
            # The pico corresponds to the depth. Not all depths have a scanner
            delay_depth = depth + delay
            key = str(depth)
            if key in self.scanners:
                scan_pos = self.scanners[key].pos_at_pico(delay_depth)
                if scan_pos == 0:
                    # It is at the top
                    collision = True
                    severity_counter += depth * self.scanners[key].sc_range
        return severity_counter, collision


# Get dict of scanner depth and range
scanners = {k: Scanner(v) for k, v in [d.split(': ') for d in data.split('\n')]}

journey = Journey(scanners)
#print("DLEAY 0: {}".format(journey.severity(delay=0)))
print("delay 1 {}".format(journey.severity(delay=152252)))
#print("delay 2 {}".format(journey.severity(delay=2)))

delayed = 0
while True:
    sev_at_del, collision = journey.severity(delay=delayed)
    #print("Severity at {} is {}".format(delayed, sev_at_del))
    if sev_at_del == 0 and not collision:
        break
    delayed += 1

print("P2: {}".format(delayed))
