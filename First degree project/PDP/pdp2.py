import xo

SIZE = 9
DET = 8

class PdpXo:
    def __init__(self,f_sign):
        self.in_f = [False] * SIZE
        self.in_e = [False] * SIZE
        self.out = [False] * SIZE

        self.sin_f = [False] * DET
        self.sin_e = [False] * DET
        self.dub_f = [False] * DET
        self.dub_e = [False] * DET
        self.emp = [True] * DET

