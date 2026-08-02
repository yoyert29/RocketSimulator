from dataclasses import dataclass

@dataclass
class Rocket:
    name: str
    mass: float
    front_area: float
    drag_coefficient: float