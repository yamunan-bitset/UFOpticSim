from .material import Material

class Lens:
    def __init__(self, material: Material, focal_length_mm: float, pos_cm2: tuple) -> None:
        self.focal_length_mm = focal_length_mm 
        self.material = material
        self.x = pos_cm2[0]
        self.y = pos_cm2[1]

    def pos(self) -> list[float]:
        return [self.x, self.y]