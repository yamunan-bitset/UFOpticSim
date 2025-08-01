from ast import Tuple

from traitlets import Int
from .pulseprofile import PulseProfile

class Laser:
    def __init__(self, beam_profile: PulseProfile, dir: tuple, pos_cm2: tuple) -> None:
        self.beam = beam_profile
        assert len(dir) == 2 and len(pos_cm2) == 2
        self.dirx = dir[0]
        self.diry = dir[1]
        self.x = pos_cm2[0]
        self.y = pos_cm2[1]

    def pos(self) -> list[float]:
        return [self.x, self.y]