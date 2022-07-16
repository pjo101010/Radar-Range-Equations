import math


class RadarRangeEquation:
    def __init__(self, power_tx=0, power_min_rx=0, rcs=0, gain_tx=0, gain_rx=0, range=0, wave_length=0):
        self.power_tx = power_tx
        self.power_min_rx = power_min_rx
        self.sigma = rcs
        self.gain_tx = gain_tx
        self.gain_rx = gain_rx
        self.range = range
        self.wave_length = wave_length
        self.c = 299792458  # m/s
        self.frequency = self.c / wave_length

    def max_detection_range(self):
        return pow((self.power_tx * self.gain_rx * self.gain_tx * pow(self.wave_length, 2) * self.sigma) /
                   (9.42 * self.power_min_rx), .25)

    def probabiltiy_of_detection(self, swerling=0):
        if swerling == 0:
            return

        elif swerling == 1:
            return (1 / self.sigma) * math.exp(-self.sigma/self.sigma)

        elif swerling == 2:
            return

        elif swerling == 3:
            return (4 / (self.sigma ** 2)) * math.exp(-2 * self.sigma/self.sigma)

        elif swerling == 4:
            return
