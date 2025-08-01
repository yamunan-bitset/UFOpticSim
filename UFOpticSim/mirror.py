from .material import Material

class Mirror:
    def __init__(self, material: Material, angle_to_horizontal: float, pos_cm2: tuple) -> None:
        self.material = material
        assert 0 <= angle_to_horizontal < 360
        self.angle = angle_to_horizontal
        self.x = pos_cm2[0]
        self.y = pos_cm2[1]

    def pos(self) -> list[float]:
        return [self.x, self.y]