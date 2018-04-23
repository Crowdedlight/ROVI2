
from math import tan

def getGSD(h, fov, pixel_width):
    GSD = (2*h*tan(fov/2))/pixel_width
    return GSD