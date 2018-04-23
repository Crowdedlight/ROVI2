class ColorInfo(object):
    RGBmean = [0, 0, 0]
    RGBstd = [0, 0, 0]
    HSVmean = [0, 0, 0]
    HSVstd = [0, 0, 0]

    def __init__(self, RGBmean, RGBstd, HSVmean, HSVstd):
        self.RGBmean = RGBmean
        self.RGBstd = RGBstd
        self.HSVmean = HSVmean
        self.HSVstd = HSVstd


